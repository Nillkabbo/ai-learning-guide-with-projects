"""
Enhanced Interactive Chatbot - Complete Solution
Chapter 3 Project

This solution demonstrates professional development practices:
- Secure API key management with .env
- Proper project structure
- Error handling
- Conversation management
"""

import os
import sys
from typing import List, Dict, Optional
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("Warning: openai not installed. Install with: pip install openai")


class Chatbot:
    """Enhanced chatbot with conversation history and context management."""
    
    def __init__(self, system_message: Optional[str] = None):
        """
        Initialize the chatbot with secure API key management.
        
        Args:
            system_message: Custom system message. Defaults to helpful assistant.
        """
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key and OPENAI_AVAILABLE:
            raise ValueError(
                "OPENAI_API_KEY not found in environment.\n"
                "Create a .env file with: OPENAI_API_KEY=your_key_here"
            )
        
        # Initialize OpenAI client
        if OPENAI_AVAILABLE:
            self.client = openai.OpenAI(api_key=api_key)
        else:
            self.client = None
        
        # Initialize conversation history
        default_system = system_message or "You are a helpful, knowledgeable assistant."
        self.conversation_history: List[Dict[str, str]] = [
            {"role": "system", "content": default_system}
        ]
        
        # Track token usage
        self.total_tokens = 0
        self.total_cost = 0.0
    
    def chat(self, user_input: str) -> str:
        """
        Send a message to the chatbot and get a response.
        
        Args:
            user_input: The user's message
            
        Returns:
            The AI's response
        """
        if not self.client:
            return "Error: OpenAI client not initialized. Check your API key."
        
        # Add user message to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        try:
            # Make API call
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.conversation_history
            )
            
            # Extract response
            ai_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({"role": "assistant", "content": ai_message})
            
            # Track usage
            if response.usage:
                self.total_tokens += response.usage.total_tokens
                # Rough cost estimate (gpt-4o-mini pricing)
                input_cost = (response.usage.prompt_tokens / 1_000_000) * 0.15
                output_cost = (response.usage.completion_tokens / 1_000_000) * 0.60
                self.total_cost += input_cost + output_cost
            
            return ai_message
            
        except openai.AuthenticationError:
            return "Error: Invalid API key. Check your .env file."
        except openai.RateLimitError:
            return "Error: Rate limit exceeded. Please wait a moment."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def clear_history(self):
        """Clear conversation history but keep system message."""
        if self.conversation_history and self.conversation_history[0]["role"] == "system":
            system_msg = self.conversation_history[0]
            self.conversation_history = [system_msg]
        else:
            self.conversation_history = []
    
    def get_token_usage(self) -> int:
        """Return total tokens used in this session."""
        return self.total_tokens
    
    def get_cost_estimate(self) -> float:
        """Return estimated cost for this session."""
        return self.total_cost


def main():
    """Main function to run the chatbot."""
    print("🤖 Enhanced AI Chatbot")
    print("Type '/help' for commands, 'quit' to exit\n")
    
    try:
        chatbot = Chatbot()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            elif user_input.lower() == '/help':
                print("\nAvailable commands:")
                print("  /help - Show this help message")
                print("  /clear - Clear conversation history")
                print("  /tokens - Show token usage")
                print("  /quit - Exit the chatbot\n")
                continue
            elif user_input.lower() == '/clear':
                chatbot.clear_history()
                print("Conversation cleared. Starting fresh.\n")
                continue
            elif user_input.lower() == '/tokens':
                tokens = chatbot.get_token_usage()
                cost = chatbot.get_cost_estimate()
                print(f"\nTokens used: {tokens:,}")
                print(f"Estimated cost: ${cost:.6f}\n")
                continue
            
            # Process message
            response = chatbot.chat(user_input)
            print(f"\nAI: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")
    
    # Display final stats
    tokens = chatbot.get_token_usage()
    cost = chatbot.get_cost_estimate()
    if tokens > 0:
        print(f"\nTotal tokens used: {tokens:,}")
        print(f"Estimated cost: ${cost:.6f}")


if __name__ == "__main__":
    main()
