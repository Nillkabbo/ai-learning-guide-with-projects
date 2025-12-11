# IoT Device Status Dashboard - Starter Code
# This is a template to help you get started. Fill in the TODOs.

import os

# TODO: Import your chosen AI library
# Option 1: import openai
# Option 2: import ollama

def interpret_device_message(message, use_openai=True):
    """
    Uses AI to interpret an IoT device status message.
    
    Args:
        message: The device status message to interpret
        use_openai: If True, use OpenAI; if False, use Ollama
    
    Returns:
        The AI's interpretation of the message
    """
    # TODO: Create system message
    # The system message should tell the AI it's an IoT expert
    system_message = {
        "role": "system",
        "content": ""  # TODO: Write the system message
    }
    
    # TODO: Create user message
    user_message = {
        "role": "user",
        "content": ""  # TODO: Format the user message with the device status
    }
    
    # TODO: Make the AI API call
    if use_openai:
        # TODO: OpenAI implementation
        # client = openai.OpenAI()
        # response = client.chat.completions.create(...)
        # return response.choices[0].message.content
        pass
    else:
        # TODO: Ollama implementation
        # response = ollama.chat(...)
        # return response["message"]["content"]
        pass
    
    return "TODO: Return AI response"

def main():
    """Main function to run the dashboard."""
    print("IoT Device Status Dashboard")
    print("=" * 40)
    print("Enter device status messages (type 'quit' to exit)\n")
    
    # TODO: Create a loop to accept user input
    while True:
        # TODO: Get user input
        user_input = input("> ")
        
        # TODO: Check if user wants to quit
        # if user_input.lower() == 'quit':
        #     break
        
        # TODO: Call interpret_device_message
        # interpretation = interpret_device_message(user_input)
        
        # TODO: Display the interpretation
        # print("\nInterpretation:")
        # print(interpretation)
        # print()
    
    print("Goodbye!")

if __name__ == "__main__":
    main()

