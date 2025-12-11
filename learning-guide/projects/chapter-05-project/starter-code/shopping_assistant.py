"""
E-Commerce Recommendation Assistant - Starter Code
Chapter 5 Project

This starter code provides a basic structure for building a shopping assistant
that uses system messages, conversation history, function calling, and streaming.
"""

import os
from typing import List, Dict, Optional

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai


# Mock product database
PRODUCTS = [
    {"name": "Logitech M705", "category": "mouse", "price": 39.99, "features": "wireless, ergonomic"},
    {"name": "Microsoft Surface Mouse", "category": "mouse", "price": 34.99, "features": "bluetooth, sleek"},
    # TODO: Add more products
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
    # TODO: Implement product search logic
    results = PRODUCTS
    
    if category:
        # TODO: Filter by category
        pass
    
    if max_price:
        # TODO: Filter by price
        pass
    
    return results


class ShoppingAssistant:
    """E-commerce recommendation assistant."""
    
    def __init__(self):
        """Initialize the shopping assistant."""
        # TODO: Load environment variables
        # TODO: Initialize OpenAI client
        # TODO: Set up system message (shopping expert persona)
        # TODO: Initialize conversation history
        pass
    
    def chat(self, user_input: str, stream: bool = False) -> str:
        """
        Chat with the shopping assistant.
        
        Args:
            user_input: User's message
            stream: Whether to stream the response
            
        Returns:
            Assistant's response
        """
        # TODO: Add user message to history
        # TODO: Define function for product search
        # TODO: Make API call with function calling
        # TODO: Handle function calls if needed
        # TODO: Add assistant response to history
        # TODO: Support streaming
        
        return "TODO: Return response"


def main():
    """Main function to run the shopping assistant."""
    print("🛍️  E-Commerce Recommendation Assistant")
    print("Type 'quit' to exit\n")
    
    # TODO: Initialize assistant
    # assistant = ShoppingAssistant()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                break
            
            # TODO: Get response (with streaming)
            # response = assistant.chat(user_input, stream=True)
            # TODO: Display streaming response
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
