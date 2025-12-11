"""
Multi-Agent IoT Management System - Complete Solution
Chapter 16 Project

Demonstrates multi-agent coordination with specialized agents.
"""

import os
from typing import Dict, List
from abc import ABC, abstractmethod
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class Agent(ABC):
    """Base agent class."""
    
    def __init__(self, name: str, client):
        self.name = name
        self.client = client
    
    @abstractmethod
    def process(self, task: Dict) -> Dict:
        """Process a task."""
        pass


class MonitoringAgent(Agent):
    """Specialized monitoring agent."""
    
    def process(self, task: Dict) -> Dict:
        """Process monitoring task."""
        prompt = f"As a monitoring specialist, analyze: {task.get('data', {})}"
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return {
                "status": "monitored",
                "agent": self.name,
                "analysis": response.choices[0].message.content
            }
        except Exception as e:
            return {"status": "error", "agent": self.name, "error": str(e)}


class DiagnosticAgent(Agent):
    """Specialized diagnostic agent."""
    
    def process(self, task: Dict) -> Dict:
        """Process diagnostic task."""
        prompt = f"As a diagnostic specialist, diagnose: {task.get('issue', '')}"
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return {
                "status": "diagnosed",
                "agent": self.name,
                "diagnosis": response.choices[0].message.content
            }
        except Exception as e:
            return {"status": "error", "agent": self.name, "error": str(e)}


class Coordinator:
    """Coordinates multiple agents."""
    
    def __init__(self, client):
        self.client = client
        self.agents = {
            "monitoring": MonitoringAgent("MonitoringAgent", client),
            "diagnostic": DiagnosticAgent("DiagnosticAgent", client)
        }
    
    def distribute_task(self, task: Dict) -> Dict:
        """Distribute task to appropriate agent."""
        task_type = task.get("type", "monitoring")
        agent = self.agents.get(task_type, self.agents["monitoring"])
        result = agent.process(task)
        return {"coordinator": "task_distributed", "result": result}


def main():
    """Main function."""
    print("🤝 Multi-Agent IoT Management System")
    print("Type 'quit' to exit\n")
    
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or not OPENAI_AVAILABLE:
        print("Error: OpenAI API key required")
        return
    
    client = openai.OpenAI(api_key=api_key)
    coordinator = Coordinator(client)
    
    while True:
        try:
            task_type = input("Task type (monitoring/diagnostic/quit): ").strip()
            if task_type.lower() == 'quit':
                break
            
            task = {"type": task_type, "data": "Sample device data"}
            result = coordinator.distribute_task(task)
            print(f"\nResult: {result}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
