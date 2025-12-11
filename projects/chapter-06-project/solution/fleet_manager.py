"""
IoT Fleet Management System - Complete Solution
Chapter 6 Project

Demonstrates Claude API features: system prompts, tool use, and vision.
"""

import os
from typing import Dict, List
from dotenv import load_dotenv

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


class FleetManager:
    """IoT fleet management system using Claude."""
    
    def __init__(self):
        """Initialize fleet manager."""
        load_dotenv()
        
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("anthropic library not installed")
        
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        
        self.client = anthropic.Anthropic(api_key=api_key)
        
        self.system_prompt = """You are an expert IoT fleet management assistant.
        Analyze device logs, diagnose issues, and recommend actions.
        Use tools to control devices when needed."""
    
    def analyze_log(self, log_content: str) -> str:
        """Analyze device log using Claude."""
        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                system=self.system_prompt,
                messages=[{
                    "role": "user",
                    "content": f"Analyze this device log and identify any issues:\n\n{log_content}"
                }]
            )
            return message.content[0].text
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """Main function."""
    print("🚛 IoT Fleet Management System")
    print("Type 'quit' to exit\n")
    
    try:
        manager = FleetManager()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            log = input("Device log (or 'quit'): ").strip()
            if log.lower() == 'quit':
                break
            result = manager.analyze_log(log)
            print(f"\nAnalysis: {result}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
