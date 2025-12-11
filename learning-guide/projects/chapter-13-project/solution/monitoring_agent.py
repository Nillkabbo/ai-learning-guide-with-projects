"""
Autonomous IoT Monitoring Agent - Complete Solution
Chapter 13 Project

Demonstrates complete agent architecture with perception, memory, reasoning, and action.
"""

import os
import time
from typing import Dict, List
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class MonitoringAgent:
    """Autonomous IoT monitoring agent."""
    
    def __init__(self):
        """Initialize agent components."""
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or not OPENAI_AVAILABLE:
            raise ValueError("OpenAI API key required")
        
        self.client = openai.OpenAI(api_key=api_key)
        self.goals = ["Monitor device health", "Detect anomalies", "Maintain optimal performance"]
        self.memory = []
        self.state = {"devices": {}, "alerts": []}
        self.system_prompt = """You are an autonomous IoT monitoring agent.
        Analyze device data, detect issues, and recommend actions.
        Be concise and actionable."""
    
    def perceive(self) -> Dict:
        """Gather information from environment."""
        # Simulate device readings
        return {
            "device_01": {"temperature": 25.5, "status": "normal"},
            "device_02": {"temperature": 95.0, "status": "warning"}
        }
    
    def remember(self, data: Dict):
        """Store information in memory."""
        self.memory.append(data)
        # Update state
        if "devices" in data:
            self.state["devices"].update(data["devices"])
    
    def reason(self, perception: Dict) -> Dict:
        """Make decisions based on perception and memory."""
        context = f"Current state: {self.state}\nRecent memory: {self.memory[-3:] if self.memory else 'None'}\nCurrent perception: {perception}"
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Analyze this situation and decide on actions:\n{context}"}
                ]
            )
            reasoning = response.choices[0].message.content
            return {"action": "investigate", "reasoning": reasoning, "target": "device_02"}
        except Exception as e:
            return {"action": "monitor", "reasoning": f"Error: {str(e)}"}
    
    def act(self, decision: Dict) -> Dict:
        """Execute actions based on decision."""
        action = decision.get("action", "monitor")
        if action == "investigate":
            return {"alert": f"Investigating {decision.get('target')}", "status": "action_taken"}
        return {"status": "monitoring"}
    
    def run_loop(self, iterations: int = 5):
        """Main agent loop."""
        print("Agent starting...\n")
        for i in range(iterations):
            print(f"--- Cycle {i+1} ---")
            
            # Perceive
            perception = self.perceive()
            print(f"Perceived: {perception}")
            
            # Remember
            self.remember({"cycle": i+1, "devices": perception})
            
            # Reason
            decision = self.reason(perception)
            print(f"Decision: {decision['action']}")
            print(f"Reasoning: {decision['reasoning'][:100]}...")
            
            # Act
            result = self.act(decision)
            print(f"Action result: {result}\n")
            
            time.sleep(1)  # Simulate time passing
        
        print("Agent cycle complete.")


def main():
    """Main function."""
    print("🤖 Autonomous IoT Monitoring Agent")
    print("Starting agent...\n")
    
    try:
        agent = MonitoringAgent()
        agent.run_loop(iterations=3)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
