"""Tests for Chapter 28 Workflow System."""
import pytest
import asyncio
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from workflow_system import WorkflowOrchestrator, TaskStatus
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_workflow_orchestrator():
    """Test workflow orchestrator."""
    orchestrator = WorkflowOrchestrator()
    
    async def task1():
        return "result1"
    
    orchestrator.add_task("task1", task1)
    assert "task1" in orchestrator.tasks


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
