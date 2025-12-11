"""
E-Commerce Recommendation Assistant - Complete Solution
Chapter 5 Project

This solution demonstrates all major OpenAI API features:
- System messages for personality
- Conversation history for context
- Function calling for product search
- Streaming for real-time responses
"""

import os
import json
from typing import List, Dict, Optional
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


# Mock product database
PRODUCTS = [
    {"name": "Logitech M705", "category": "mouse", "price": 39.99, "features": "wireless, ergonomic, long battery"},
    {"name": "Microsoft Surface Mouse", "category": "mouse", "price": 34.99, "features": "bluetooth, sleek, travel"},
    {"name": "Razer DeathAdder", "category": "mouse", "price": 69.99, "features": "gaming, RGB, precision"},
    {"name": "Apple Magic Keyboard", "category": "keyboard", "price": 99.99, "features": "wireless, slim, mac"},
    {"name": "Mechanical Keyboard Pro", "category": "keyboard", "price": 129.99, "features": "mechanical, RGB, gaming"},
]


def search_products(category: Optional[str] = None, max_price: Optional[float] = None) -> List[Dict]:
    """
    Search products by category and price.
    
    Args:
        category: Product category to filter
        max_price: Maximum price
        
    Returns:
        List of matching products
    """
    results = PRODUCTS.copy()
    
    if category:
        results = [p for p in results if p["category"].lower() == category.lower()]
    
    if max_price:
        results = [p for p in results if p["price"] <= max_price]
    
    return results


class ShoppingAssistant:
    """E-commerce recommendation assistant."""
    
    def __init__(self):
        """Initialize the shopping assistant."""
        load_dotenv()
        
        if not OPENAI_AVAILABLE:
            raise ImportError("openai library not installed")
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        
        self.client = openai.OpenAI(api_key=api_key)
        
        # System message creates shopping expert personality
        self.system_message = """You are a friendly, knowledgeable shopping assistant for an electronics store.
        You help customers find the perfect products by understanding their needs and preferences.
        Use the search_products function to find products when customers ask about specific items.
        Be conversational, helpful, and focus on matching products to customer needs."""
        
        self.conversation_history = [
            {"role": "system", "content": self.system_message}
        ]
        
        # Define function for product search
        self.functions = [
            {
                "type": "function",
                "function": {
                    "name": "search_products",
                    "description": "Search for products by category and maximum price",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "category": {
                                "type": "string",
                                "description": "Product category (e.g., mouse, keyboard)"
                            },
                            "max_price": {
                                "type": "number",
                                "description": "Maximum price in dollars"
                            }
                        }
                    }
                }
            }
        ]
    
    def chat(self, user_input: str, stream: bool = False) -> str:
        """
        Chat with the shopping assistant.
        
        Args:
            user_input: User's message
            stream: Whether to stream the response
            
        Returns:
            Assistant's response
        """
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        try:
            # Make API call with function calling
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.conversation_history,
                tools=self.functions,
                tool_choice="auto",
                stream=stream
            )
            
            if stream:
                return self._handle_streaming_response(response)
            else:
                return self._handle_response(response)
                
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _handle_streaming_response(self, response) -> str:
        """Handle streaming response."""
        full_response = ""
        print("\nAssistant: ", end="", flush=True)
        
        for chunk in response:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                full_response += content
            
            # Check for function calls in streaming
            if chunk.choices[0].delta.tool_calls:
                # Function calling in streaming is complex, handle separately
                pass
        
        print()  # New line after streaming
        self.conversation_history.append({"role": "assistant", "content": full_response})
        return full_response
    
    def _handle_response(self, response) -> str:
        """Handle non-streaming response with function calling."""
        message = response.choices[0].message
        
        # Check if function was called
        if message.tool_calls:
            # Add assistant message with tool calls
            self.conversation_history.append(message)
            
            # Execute function calls
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                if function_name == "search_products":
                    results = search_products(
                        category=function_args.get("category"),
                        max_price=function_args.get("max_price")
                    )
                    
                    # Add function result to conversation
                    self.conversation_history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(results)
                    })
            
            # Get final response with function results
            final_response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.conversation_history
            )
            
            ai_message = final_response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": ai_message})
            return ai_message
        else:
            # No function call, just return response
            ai_message = message.content
            self.conversation_history.append({"role": "assistant", "content": ai_message})
            return ai_message


def main():
    """Main function to run the shopping assistant."""
    print("🛍️  E-Commerce Recommendation Assistant")
    print("Type 'quit' to exit\n")
    
    try:
        assistant = ShoppingAssistant()
    except Exception as e:
        print(f"Error initializing assistant: {e}")
        return
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            if not user_input:
                continue
            
            # Use streaming for better UX
            assistant.chat(user_input, stream=True)
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
