"""
Autonomous IoT Monitoring Agent - Starter Code
Chapter 13 Project

This starter code provides a basic structure for building an autonomous agent
with perception, memory, reasoning, and action components.
"""

import os
from typing import Dict, List, Optional

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai


class MonitoringAgent:
    """Autonomous IoT monitoring agent."""
    
    def __init__(self):
        """Initialize agent components."""
        # TODO: Initialize perception system
        # TODO: Initialize memory system
        # TODO: Initialize reasoning engine (LLM client)
        # TODO: Initialize action system
        # TODO: Set goals
        self.goals = []
        self.memory = []
        self.state = {}
    
    def perceive(self) -> Dict:
        """
        Gather information from environment.
        
        Returns:
            Perceived data
        """
        # TODO: Read device sensors
        # TODO: Check device status
        # TODO: Monitor environment
        return {}
    
    def remember(self, data: Dict):
        """
        Store information in memory.
        
        Args:
            data: Data to store
        """
        # TODO: Add to memory
        # TODO: Update state
        pass
    
    def reason(self, perception: Dict) -> Dict:
        """
        Make decisions based on perception and memory.
        
        Args:
            perception: Current perception data
            
        Returns:
            Decision/plan
        """
        # TODO: Use LLM to reason about situation
        # TODO: Evaluate goals
        # TODO: Plan actions
        return {"action": "monitor", "reasoning": "TODO"}
    
    def act(self, decision: Dict) -> Dict:
        """
        Execute actions based on decision.
        
        Args:
            decision: Decision from reasoning
            
        Returns:
            Action result
        """
        # TODO: Execute device control
        # TODO: Generate alerts
        # TODO: Create reports
        return {"status": "TODO"}
    
    def run_loop(self):
        """Main agent loop."""
        # TODO: Implement agent loop:
        # 1. Perceive
        # 2. Remember
        # 3. Reason
        # 4. Act
        # 5. Repeat
        pass


def main():
    """Main function."""
    print("🤖 Autonomous IoT Monitoring Agent")
    print("Starting agent...\n")
    
    # TODO: Initialize agent
    # agent = MonitoringAgent()
    # agent.run_loop()


if __name__ == "__main__":
    main()
