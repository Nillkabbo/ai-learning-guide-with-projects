"""
Multi-Agent IoT Management System - Starter Code
Chapter 16 Project

This starter code provides a basic structure for building a multi-agent system
with specialized agents and coordination.
"""

import os
from typing import Dict, List
from abc import ABC, abstractmethod

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai


class Agent(ABC):
    """Base agent class."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def process(self, task: Dict) -> Dict:
        """Process a task."""
        pass


class MonitoringAgent(Agent):
    """Specialized monitoring agent."""
    
    def process(self, task: Dict) -> Dict:
        """Process monitoring task."""
        # TODO: Implement monitoring logic
        return {"status": "monitored", "agent": self.name}


class DiagnosticAgent(Agent):
    """Specialized diagnostic agent."""
    
    def process(self, task: Dict) -> Dict:
        """Process diagnostic task."""
        # TODO: Implement diagnostic logic
        return {"status": "diagnosed", "agent": self.name}


class Coordinator:
    """Coordinates multiple agents."""
    
    def __init__(self):
        # TODO: Initialize agents
        self.agents = {}
    
    def distribute_task(self, task: Dict) -> Dict:
        """
        Distribute task to appropriate agent.
        
        Args:
            task: Task to distribute
            
        Returns:
            Aggregated results
        """
        # TODO: Route task to appropriate agent
        # TODO: Collect results
        # TODO: Return aggregated result
        return {}


def main():
    """Main function."""
    print("🤝 Multi-Agent IoT Management System")
    print("Type 'quit' to exit\n")
    
    # TODO: Initialize coordinator
    # TODO: Implement main loop


if __name__ == "__main__":
    main()
