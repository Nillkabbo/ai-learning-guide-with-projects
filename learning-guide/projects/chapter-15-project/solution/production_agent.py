"""
Production Industrial Automation Agent - Complete Solution
Chapter 15 Project

Demonstrates production patterns: state persistence, observability, error handling.
"""

import os
import json
import logging
from typing import Dict
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ProductionAgent:
    """Production-ready agent with persistence and observability."""
    
    def __init__(self, state_file: str = "agent_state.json"):
        """Initialize agent."""
        load_dotenv()
        
        self.state_file = state_file
        self.state = self.load_state()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or not OPENAI_AVAILABLE:
            raise ValueError("OpenAI API key required")
        
        self.client = openai.OpenAI(api_key=api_key)
        logger.info("Agent initialized", extra={"state_file": state_file})
    
    def save_state(self):
        """Persist agent state to file."""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(self.state, f, indent=2)
            logger.info("State saved", extra={"state_file": self.state_file})
        except Exception as e:
            logger.error("Failed to save state", exc_info=e)
    
    def load_state(self) -> Dict:
        """Load agent state from file."""
        try:
            if os.path.exists(self.state_file):
                with open(self.state_file, 'r') as f:
                    state = json.load(f)
                logger.info("State loaded", extra={"state_file": self.state_file})
                return state
        except Exception as e:
            logger.error("Failed to load state", exc_info=e)
        return {"cycle": 0, "actions": []}
    
    def log_action(self, action: str, data: Dict):
        """Log agent action."""
        logger.info("Action executed", extra={"action": action, "data": data})
        self.state["actions"].append({"action": action, "data": data})
    
    def handle_error(self, error: Exception, context: Dict):
        """Handle errors gracefully."""
        logger.error("Error occurred", exc_info=error, extra=context)
        self.state.setdefault("errors", []).append({
            "error": str(error),
            "context": context
        })
        self.save_state()
    
    def run(self, iterations: int = 3):
        """Main agent run loop."""
        logger.info("Agent started", extra={"iterations": iterations})
        
        try:
            for i in range(iterations):
                self.state["cycle"] = i + 1
                logger.info("Agent cycle", extra={"cycle": i + 1})
                
                # Simulate agent work
                self.log_action("monitor", {"device": "device_01"})
                
                # Save state periodically
                if (i + 1) % 2 == 0:
                    self.save_state()
            
            self.save_state()
            logger.info("Agent completed")
        except Exception as e:
            self.handle_error(e, {"iterations": iterations})


def main():
    """Main function."""
    print("🏭 Production Industrial Automation Agent")
    print("Starting agent...\n")
    
    try:
        agent = ProductionAgent()
        agent.run(iterations=3)
        print("\nAgent completed. Check agent_state.json for persisted state.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
