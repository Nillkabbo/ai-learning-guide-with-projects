"""
Enhanced Interactive Chatbot - Starter Code
Chapter 3 Project

This starter code provides a basic structure. Fill in the TODOs to build
a complete chatbot with professional development practices.
"""

import os
from typing import List, Dict

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai


class Chatbot:
    """Enhanced chatbot with conversation history and context management."""
    
    def __init__(self):
        """Initialize the chatbot with secure API key management."""
        # TODO: Load environment variables
        # load_dotenv()
        
        # TODO: Initialize OpenAI client with API key from environment
        # api_key = os.getenv("OPENAI_API_KEY")
        # if not api_key:
        #     raise ValueError("OPENAI_API_KEY not found in environment")
        # self.client = openai.OpenAI(api_key=api_key)
        
        # TODO: Initialize conversation history with system message
        self.conversation_history: List[Dict[str, str]] = [
            # {"role": "system", "content": "You are a helpful assistant."}
        ]
        
        # TODO: Track token usage (optional, from Chapter 2)
        self.total_tokens = 0
    
    def chat(self, user_input: str) -> str:
        """
        Send a message to the chatbot and get a response.
        
        Args:
            user_input: The user's message
            
        Returns:
            The AI's response
        """
        # TODO: Add user message to conversation history
        # self.conversation_history.append({"role": "user", "content": user_input})
        
        # TODO: Make API call
        # response = self.client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=self.conversation_history
        # )
        
        # TODO: Extract response
        # ai_message = response.choices[0].message.content
        
        # TODO: Add assistant response to history
        # self.conversation_history.append({"role": "assistant", "content": ai_message})
        
        # TODO: Track tokens (optional)
        # self.total_tokens += response.usage.total_tokens
        
        return "TODO: Return AI response"
    
    def clear_history(self):
        """Clear conversation history but keep system message."""
        # TODO: Keep system message, remove others
        if self.conversation_history and self.conversation_history[0]["role"] == "system":
            system_msg = self.conversation_history[0]
            self.conversation_history = [system_msg]
        else:
            self.conversation_history = []
    
    def get_token_usage(self) -> int:
        """Return total tokens used in this session."""
        return self.total_tokens


def main():
    """Main function to run the chatbot."""
    print("🤖 Enhanced AI Chatbot")
    print("Type '/help' for commands, 'quit' to exit\n")
    
    # TODO: Initialize chatbot
    # chatbot = Chatbot()
    
    while True:
        try:
            # TODO: Get user input
            user_input = input("You: ").strip()
            
            # TODO: Handle commands (/help, /clear, /quit)
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            # TODO: Process message and display response
            # response = chatbot.chat(user_input)
            # print(f"\nAI: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")
    
    # TODO: Display token usage
    # print(f"Total tokens used: {chatbot.get_token_usage()}")


if __name__ == "__main__":
    main()
