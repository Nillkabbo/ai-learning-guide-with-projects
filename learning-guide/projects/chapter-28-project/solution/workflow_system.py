"""
Automated IoT Incident Response Workflow - Complete Solution
Chapter 28 Project

Demonstrates workflow orchestration: DAGs, error recovery, human-in-the-loop.
"""

import asyncio
from typing import Dict, List, Callable, Optional
from enum import Enum
from datetime import datetime
import os
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

load_dotenv()


class TaskStatus(Enum):
    """Task status."""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    WAITING_HUMAN = "waiting_human"


class WorkflowOrchestrator:
    """Workflow orchestrator with DAG support."""
    
    def __init__(self):
        """Initialize orchestrator."""
        self.tasks: Dict[str, Callable] = {}
        self.dependencies: Dict[str, List[str]] = {}
        self.task_status: Dict[str, TaskStatus] = {}
        self.task_results: Dict[str, any] = {}
        self.human_approvals: Dict[str, bool] = {}
    
    def add_task(self, task_id: str, task_func: Callable, depends_on: List[str] = None):
        """Add task to workflow."""
        self.tasks[task_id] = task_func
        self.dependencies[task_id] = depends_on or []
        self.task_status[task_id] = TaskStatus.PENDING
    
    def can_execute(self, task_id: str) -> bool:
        """Check if task can be executed (dependencies met)."""
        deps = self.dependencies.get(task_id, [])
        return all(
            self.task_status.get(dep) == TaskStatus.SUCCESS
            for dep in deps
        )
    
    async def execute_task(self, task_id: str) -> any:
        """Execute a single task."""
        if task_id not in self.tasks:
            raise ValueError(f"Task {task_id} not found")
        
        self.task_status[task_id] = TaskStatus.RUNNING
        
        try:
            task_func = self.tasks[task_id]
            if asyncio.iscoroutinefunction(task_func):
                result = await task_func()
            else:
                result = task_func()
            
            self.task_status[task_id] = TaskStatus.SUCCESS
            self.task_results[task_id] = result
            return result
        except Exception as e:
            self.task_status[task_id] = TaskStatus.FAILED
            self.task_results[task_id] = {"error": str(e)}
            raise
    
    async def wait_for_human_approval(self, task_id: str) -> bool:
        """Wait for human approval (simulated)."""
        self.task_status[task_id] = TaskStatus.WAITING_HUMAN
        print(f"[HUMAN-IN-THE-LOOP] Task {task_id} requires approval")
        # Simulate approval after delay
        await asyncio.sleep(1)
        approval = True  # In production: actual human input
        self.human_approvals[task_id] = approval
        return approval
    
    async def execute_workflow(self, start_tasks: List[str]) -> Dict:
        """Execute workflow starting from given tasks."""
        executed = set()
        queue = start_tasks.copy()
        
        while queue:
            # Find tasks ready to execute
            ready_tasks = [
                task_id for task_id in queue
                if self.can_execute(task_id) and task_id not in executed
            ]
            
            if not ready_tasks:
                # Check for human approvals needed
                waiting = [
                    task_id for task_id, status in self.task_status.items()
                    if status == TaskStatus.WAITING_HUMAN
                ]
                if waiting:
                    for task_id in waiting:
                        approved = await self.wait_for_human_approval(task_id)
                        if approved:
                            self.task_status[task_id] = TaskStatus.SUCCESS
                else:
                    break  # Deadlock or all done
            
            # Execute ready tasks
            for task_id in ready_tasks:
                try:
                    await self.execute_task(task_id)
                    executed.add(task_id)
                    queue.remove(task_id)
                    
                    # Add dependent tasks to queue
                    for next_task, deps in self.dependencies.items():
                        if task_id in deps and next_task not in queue:
                            queue.append(next_task)
                except Exception as e:
                    print(f"Task {task_id} failed: {e}")
        
        return {
            "status": "completed",
            "results": self.task_results,
            "task_status": {k: v.value for k, v in self.task_status.items()}
        }


# Example workflow tasks
async def analyze_incident():
    """Analyze incident."""
    await asyncio.sleep(0.5)
    return {"severity": "high", "device": "sensor_01"}


async def notify_team():
    """Notify team."""
    await asyncio.sleep(0.3)
    return {"notified": True}


async def take_action():
    """Take automated action."""
    await asyncio.sleep(0.5)
    return {"action": "device_restarted"}


def main():
    """Main function."""
    print("🔄 Automated IoT Incident Response Workflow")
    print("=" * 50)
    
    orchestrator = WorkflowOrchestrator()
    
    # Define workflow DAG
    orchestrator.add_task("analyze", analyze_incident)
    orchestrator.add_task("notify", notify_team, depends_on=["analyze"])
    orchestrator.add_task("action", take_action, depends_on=["analyze", "notify"])
    
    # Execute workflow
    async def run():
        results = await orchestrator.execute_workflow(["analyze"])
        print("\nWorkflow Results:")
        print(results)
    
    asyncio.run(run())


if __name__ == "__main__":
    main()
