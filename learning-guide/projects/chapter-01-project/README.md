# Chapter 1 Project: IoT Device Status Dashboard

## Project Overview

Build a command-line tool that uses AI to interpret and explain IoT device status messages in plain English. This project reinforces all the key concepts from Chapter 1: making AI calls, using message roles, and building a practical application.

## Learning Objectives

By completing this project, you will:
- Write Python code to interact with AI models (OpenAI or Ollama)
- Use system messages to guide AI behavior
- Structure conversations with proper message roles
- Build a practical, real-world application
- Handle user input and format output
- Understand the basic pattern of AI applications

## Project Type

**Standalone** - This project is self-contained and focuses on Chapter 1 concepts. However, the skills you learn here will be used in all future projects.

## Prerequisites

- Python 3.8 or higher installed
- OpenAI API key (or Ollama installed and running)
- Basic Python knowledge (variables, functions, imports, if/else)
- Code editor set up

## Project Requirements

### Core Features (Must Have)

1. **AI Integration**
   - Connect to either OpenAI or Ollama
   - Use a system message to set the AI's role as an IoT expert
   - Send device status messages to the AI
   - Display the AI's interpretation

2. **Command-Line Interface**
   - Accept device status messages as input
   - Display formatted output
   - Handle multiple messages in one session

3. **Message Structure**
   - Proper use of system, user, and assistant roles
   - Maintain conversation context when needed

### Extended Features (Nice to Have)

- Support for multiple device types
- Color-coded output based on status severity
- Save conversation history
- Batch processing of multiple messages
- Error handling for invalid inputs
- Configuration file for API keys/model selection

## Project Structure

```
chapter-01-project/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── starter-code/         # Optional starter templates
│   └── main.py
├── solution/              # Complete solution (for reference)
│   └── iot_dashboard.py
├── tests/                 # Test cases
│   └── test_dashboard.py
└── docs/                  # Additional documentation
    └── design.md
```

## Step-by-Step Instructions

### Step 1: Set Up Your Environment

1. Create a new Python file: `iot_dashboard.py`
2. Install required libraries:
   ```bash
   pip install openai
   # OR
   pip install ollama
   ```
3. Set up your API key (OpenAI) or ensure Ollama is running

### Step 2: Create the Basic Structure

Start with this skeleton:

```python
# iot_dashboard.py
import os
# Import your chosen AI library (openai or ollama)

def interpret_device_message(message):
    """Uses AI to interpret an IoT device status message."""
    # TODO: Implement this function
    pass

def main():
    """Main function to run the dashboard."""
    print("IoT Device Status Dashboard")
    print("=" * 40)
    # TODO: Implement main loop
    pass

if __name__ == "__main__":
    main()
```

### Step 3: Implement the AI Call

**Checkpoint 1**: Can you make a basic AI call?

Implement the `interpret_device_message` function:
- Create a system message describing the AI's role
- Create a user message with the device status
- Make the API call
- Extract and return the response

**Test**: Try with a simple message like "TEMP_SENSOR_01: 85.2C STATUS:WARNING"

### Step 4: Build the User Interface

**Checkpoint 2**: Can users interact with your tool?

Implement the `main` function:
- Display a welcome message
- Create a loop to accept multiple messages
- Call `interpret_device_message` for each input
- Display the AI's response
- Allow users to quit

**Test**: Run the program and try entering different device messages

### Step 5: Add Polish

**Checkpoint 3**: Is your tool user-friendly?

Add:
- Clear prompts for user input
- Formatted output (maybe with separators)
- Error handling (what if API call fails?)
- Option to quit gracefully
- Better formatting of AI responses

### Step 6: Extend (Optional)

Try adding:
- Support for both OpenAI and Ollama (let user choose)
- Color coding for different status types
- Ability to process multiple messages at once
- Save conversation to a file

## Project Milestones

### Milestone 1: Basic AI Call (30 minutes)
- [ ] Can make an AI API call
- [ ] System message is set correctly
- [ ] Can get a response from AI
- [ ] Response is displayed

### Milestone 2: User Interface (30 minutes)
- [ ] User can input device messages
- [ ] Program processes input
- [ ] Output is displayed clearly
- [ ] Can handle multiple messages

### Milestone 3: Error Handling (20 minutes)
- [ ] Handles API errors gracefully
- [ ] Handles invalid input
- [ ] Provides helpful error messages
- [ ] Program doesn't crash on errors

### Milestone 4: Polish (20 minutes)
- [ ] Code is clean and readable
- [ ] Comments explain key parts
- [ ] User experience is smooth
- [ ] Output is well-formatted

### Milestone 5: Extension (Optional, 30+ minutes)
- [ ] Added at least one extended feature
- [ ] Feature works correctly
- [ ] Code remains readable

## Example Usage

```
$ python iot_dashboard.py

IoT Device Status Dashboard
========================================
Enter device status messages (type 'quit' to exit)

> TEMP_SENSOR_01: 85.2C STATUS:WARNING

Interpretation:
This message indicates that temperature sensor TEMP_SENSOR_01 is 
reporting a temperature of 85.2 degrees Celsius with a WARNING status. 
This suggests the temperature has exceeded normal operating parameters 
and may require attention to prevent potential overheating issues.

> HUMIDITY_SENSOR_02: 45% STATUS:OK

Interpretation:
Humidity sensor HUMIDITY_SENSOR_02 is reporting a humidity level of 
45%, which is within normal operating range (STATUS:OK). This is a 
healthy reading that doesn't require any immediate action.

> quit
Goodbye!
```

## Testing Your Project

### Manual Testing

Test with these device messages:
1. `TEMP_SENSOR_01: 85.2C STATUS:WARNING`
2. `HUMIDITY_SENSOR_02: 45% STATUS:OK`
3. `PRESSURE_SENSOR_03: 1200 PSI STATUS:CRITICAL`
4. `MOTION_SENSOR_04: DETECTED STATUS:INFO`
5. `BATTERY_LEVEL: 15% STATUS:LOW`

### What to Check

- Does the AI provide helpful interpretations?
- Are error messages clear?
- Can you quit the program easily?
- Does it handle edge cases (empty input, very long messages)?
- Is the code readable and well-commented?

## Success Criteria

Your project is successful if:
- ✅ Code runs without errors
- ✅ AI correctly interprets device messages
- ✅ System message effectively guides AI behavior
- ✅ User interface is clear and functional
- ✅ You can explain how your code works
- ✅ Code is readable and well-commented

## Common Challenges and Solutions

**Challenge**: "I don't know where to start"
- **Solution**: Start with Milestone 1. Just get a basic AI call working first.

**Challenge**: "The AI response is too generic"
- **Solution**: Improve your system message. Be more specific about what you want.

**Challenge**: "I get API errors"
- **Solution**: Check your API key is set correctly (OpenAI) or Ollama is running.

**Challenge**: "The output is messy"
- **Solution**: Add formatting, use separators, maybe add colors.

**Challenge**: "I want to add features but don't know how"
- **Solution**: Break it down. What's the smallest version of that feature? Start there.

## Extension Ideas

Once you've completed the core project, try:

1. **Multi-Device Support**: Handle different device types with different interpretations
2. **Severity Detection**: Automatically detect if a message indicates a critical issue
3. **History**: Save all interpretations to a file
4. **Batch Mode**: Process a file of device messages at once
5. **Interactive Mode**: Ask follow-up questions about device status
6. **Web Interface**: Convert to a simple web app (if you know Flask/FastAPI)

## Getting Help

If you're stuck:
1. Review the chapter guide for explanations
2. Check the starter code for hints
3. Look at the solution (but try to build it yourself first!)
4. Review Chapter 1 concepts
5. Experiment—sometimes trying things helps you understand

## Reflection Questions

After completing the project, ask yourself:

1. What was the hardest part? Why?
2. What did you learn about AI interactions?
3. How did the system message affect the AI's responses?
4. What would you do differently next time?
5. What feature would you add if you had more time?

## Next Steps

After completing this project:
- Review any concepts that were unclear
- Experiment with different system messages
- Try the extension ideas
- Prepare for Chapter 2 (tokens, embeddings, context windows)

---

**Remember**: The goal isn't perfection—it's understanding. If your code works and you can explain it, you've succeeded!

