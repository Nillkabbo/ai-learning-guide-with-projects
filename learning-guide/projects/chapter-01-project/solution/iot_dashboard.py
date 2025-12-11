# IoT Device Status Dashboard - Complete Solution
# This is a reference solution. Try to build your own first!

import os
import sys

# Try to import OpenAI, fall back to Ollama if not available
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

def interpret_device_message(message, use_openai=None):
    """
    Uses AI to interpret an IoT device status message.
    
    Args:
        message: The device status message to interpret
        use_openai: If True, use OpenAI; if False, use Ollama; if None, auto-detect
    
    Returns:
        The AI's interpretation of the message
    """
    # Auto-detect which library is available
    if use_openai is None:
        use_openai = OPENAI_AVAILABLE
    
    # System message sets the AI's role and behavior
    system_message = {
        "role": "system",
        "content": """You are an expert IoT monitoring assistant. Your job is to translate 
raw device status messages into clear, human-readable explanations. Explain what the 
message means, what the status indicates, and whether any action is required. Be 
concise but informative."""
    }
    
    # User message contains the device status to interpret
    user_message = {
        "role": "user",
        "content": f"Please explain what this device message means: '{message}'"
    }
    
    messages = [system_message, user_message]
    
    try:
        if use_openai and OPENAI_AVAILABLE:
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            return response.choices[0].message.content
        elif OLLAMA_AVAILABLE:
            response = ollama.chat(
                model="llama2",  # or mistral, codellama, etc.
                messages=messages
            )
            return response["message"]["content"]
        else:
            return "Error: Neither OpenAI nor Ollama is available. Please install one."
    except Exception as e:
        return f"Error interpreting message: {str(e)}"

def main():
    """Main function to run the dashboard."""
    print("IoT Device Status Dashboard")
    print("=" * 40)
    
    # Check which AI library is available
    if OPENAI_AVAILABLE:
        print("Using OpenAI (gpt-4o-mini)")
    elif OLLAMA_AVAILABLE:
        print("Using Ollama (llama2)")
    else:
        print("Error: No AI library available!")
        print("Install with: pip install openai  OR  pip install ollama")
        sys.exit(1)
    
    print("\nEnter device status messages (type 'quit' to exit)\n")
    
    while True:
        try:
            user_input = input("> ").strip()
            
            # Check if user wants to quit
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            # Skip empty input
            if not user_input:
                continue
            
            # Interpret the message
            interpretation = interpret_device_message(user_input)
            
            # Display the interpretation
            print("\nInterpretation:")
            print("-" * 40)
            print(interpretation)
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")
    
    print("Goodbye!")

if __name__ == "__main__":
    main()

