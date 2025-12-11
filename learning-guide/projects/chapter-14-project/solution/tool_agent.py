"""
Tool-Enabled IoT Agent - Complete Solution
Chapter 14 Project

Demonstrates tool-use loop, tool registry, and secure execution.
"""

import os
import json
from typing import Dict, List
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


def control_device(device_id: str, action: str) -> str:
    """Control IoT device (mock implementation)."""
    return f"Device {device_id}: {action} executed"


def get_device_status(device_id: str) -> str:
    """Get device status (mock implementation)."""
    return f"Device {device_id}: Status OK"


class ToolAgent:
    """Tool-enabled IoT agent."""
    
    def __init__(self):
        """Initialize agent."""
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or not OPENAI_AVAILABLE:
            raise ValueError("OpenAI API key required")
        
        self.client = openai.OpenAI(api_key=api_key)
        
        # Define tools
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "control_device",
                    "description": "Control an IoT device",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "device_id": {"type": "string"},
                            "action": {"type": "string", "enum": ["restart", "stop", "start"]}
                        },
                        "required": ["device_id", "action"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_device_status",
                    "description": "Get status of an IoT device",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "device_id": {"type": "string"}
                        },
                        "required": ["device_id"]
                    }
                }
            }
        ]
        
        self.messages = [
            {"role": "system", "content": "You are an IoT management assistant. Use tools to help users."}
        ]
    
    def tool_use_loop(self, user_input: str) -> str:
        """Execute tool-use loop."""
        self.messages.append({"role": "user", "content": user_input})
        
        max_iterations = 5
        for _ in range(max_iterations):
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.messages,
                tools=self.tools,
                tool_choice="auto"
            )
            
            message = response.choices[0].message
            self.messages.append(message)
            
            if message.tool_calls:
                # Execute tools
                for tool_call in message.tool_calls:
                    func_name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)
                    
                    if func_name == "control_device":
                        result = control_device(args["device_id"], args["action"])
                    elif func_name == "get_device_status":
                        result = get_device_status(args["device_id"])
                    else:
                        result = "Unknown tool"
                    
                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    })
            else:
                # No more tool calls, return final response
                return message.content
        
        return "Max iterations reached"


def main():
    """Main function."""
    print("🔧 Tool-Enabled IoT Agent")
    print("Type 'quit' to exit\n")
    
    try:
        agent = ToolAgent()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() == 'quit':
                break
            
            if not user_input:
                continue
            
            response = agent.tool_use_loop(user_input)
            print(f"\nAgent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
