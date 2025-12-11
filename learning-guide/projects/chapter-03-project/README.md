# Chapter 3 Project: Enhanced Interactive Chatbot

## Project Overview

Build an enhanced version of the chapter's chatbot with additional features like conversation saving, context management, and better error handling. This project reinforces professional development practices and applies concepts from Chapters 1-3.

## Learning Objectives

By completing this project, you will:
- Set up a professional development environment
- Implement secure API key management
- Build a well-structured Python project
- Create a feature-rich chatbot application
- Practice professional coding practices
- Apply context management from Chapter 2

## Project Type

**Cumulative** - Builds on Chapters 1-2, extends the basic chatbot with professional features.

## Prerequisites

- Completed Chapters 1-3
- Python 3.9+ installed
- OpenAI API key (or Ollama installed)
- Understanding of virtual environments
- Basic Python OOP knowledge

## Project Requirements

### Core Features (Must Have)

1. **Professional Setup**
   - Virtual environment
   - Secure API key management (.env)
   - Proper project structure
   - requirements.txt

2. **Enhanced Chatbot**
   - Conversation history management
   - System message configuration
   - Error handling
   - Clean user interface

3. **Context Management**
   - Token counting (from Chapter 2)
   - Context window management
   - Conversation trimming when needed

### Extended Features (Nice to Have)

- Save/load conversations
- Multiple conversation sessions
- Export conversation history
- Custom system prompts
- Token usage tracking
- Cost estimation
- Conversation search
- Command shortcuts (/help, /clear, /save)

## Project Structure

```
chapter-03-project/
├── README.md
├── requirements.txt
├── .env                    # Your API key (not committed)
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── chatbot.py         # Main chatbot class
│   ├── config.py           # Configuration management
│   └── utils.py            # Utility functions
├── data/
│   └── conversations/     # Saved conversations
├── tests/
│   └── test_chatbot.py
└── main.py                # Entry point
```

## Step-by-Step Instructions

### Step 1: Set Up Environment

**Checkpoint 1**: Is your environment properly configured?

1. Create project directory
2. Create virtual environment
3. Activate virtual environment
4. Install dependencies
5. Set up `.env` file
6. Create `.gitignore`

### Step 2: Project Structure

**Checkpoint 2**: Is your project well-organized?

1. Create directory structure
2. Set up `requirements.txt`
3. Create initial Python files
4. Add basic imports

### Step 3: Core Chatbot

**Checkpoint 3**: Does the basic chatbot work?

1. Implement Chatbot class
2. Add conversation history
3. Implement message sending
4. Create interactive loop
5. Test basic functionality

### Step 4: Enhanced Features

**Checkpoint 4**: Are advanced features working?

1. Add context management
2. Implement token counting
3. Add error handling
4. Create command system (/help, /clear)
5. Add conversation saving

### Step 5: Polish

**Checkpoint 5**: Is everything professional?

1. Add documentation
2. Improve error messages
3. Add user-friendly features
4. Test thoroughly
5. Clean up code

## Project Milestones

### Milestone 1: Environment Setup (30 minutes)
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] API key secured
- [ ] Project structure created

### Milestone 2: Basic Chatbot (1 hour)
- [ ] Chatbot class implemented
- [ ] Conversation works
- [ ] Error handling added
- [ ] Basic UI functional

### Milestone 3: Context Management (45 minutes)
- [ ] Token counting integrated
- [ ] Context window management
- [ ] Conversation trimming
- [ ] Token usage displayed

### Milestone 4: Enhanced Features (1 hour)
- [ ] Conversation saving
- [ ] Command system
- [ ] Better error handling
- [ ] User-friendly features

### Milestone 5: Polish (30 minutes)
- [ ] Code documented
- [ ] Tests written (optional)
- [ ] README updated
- [ ] Code cleaned up

## Example Usage

```
$ python main.py

🤖 Enhanced AI Chatbot
Type '/help' for commands, 'quit' to exit

You: Hello! Can you help me learn Python?

AI: Of course! I'd be happy to help you learn Python. What would you like to know?

You: What's a good first project?

AI: A great first Python project is building a simple calculator or a to-do list application...

Tokens used: 245 | Context: 89% full

You: /save my_python_learning

Conversation saved to: data/conversations/my_python_learning.json

You: /clear

Conversation cleared. Starting fresh.

You: /help

Available commands:
  /help - Show this help message
  /clear - Clear conversation history
  /save <name> - Save current conversation
  /load <name> - Load a saved conversation
  /tokens - Show token usage
  /quit - Exit the chatbot

You: quit

👋 Goodbye! Total tokens used: 1,234
```

## Testing Your Project

### Test Cases

1. **Basic Functionality**
   - Can start chatbot
   - Can send messages
   - Receives responses
   - Can quit gracefully

2. **Context Management**
   - Token counting works
   - Context trimming when needed
   - System message preserved
   - Long conversations handled

3. **Commands**
   - /help shows help
   - /clear clears history
   - /save saves conversation
   - /load loads conversation
   - Invalid commands handled

4. **Error Handling**
   - API errors handled
   - Network errors handled
   - Invalid input handled
   - File errors handled

### What to Check

- Does everything work as expected?
- Are errors handled gracefully?
- Is the code well-organized?
- Are API keys secure?
- Is the user experience smooth?

## Success Criteria

Your project is successful if:
- ✅ Environment is properly set up
- ✅ API keys are secure
- ✅ Chatbot functions correctly
- ✅ Context management works
- ✅ Enhanced features are implemented
- ✅ Code is professional and documented
- ✅ Project structure is clean

## Common Challenges and Solutions

**Challenge**: "Virtual environment not activating"
- **Solution**: Check you're using the right command for your OS

**Challenge**: "API key not loading"
- **Solution**: Verify .env file exists, is in right location, and has correct variable name

**Challenge**: "Context management is confusing"
- **Solution**: Start simple—just trim when over limit. Add sophistication later.

**Challenge**: "Commands not working"
- **Solution**: Check input parsing, make sure you're checking for '/' prefix

**Challenge**: "Saving conversations is hard"
- **Solution**: Use JSON format, save to a data/ directory

## Extension Ideas

1. **Web Interface**: Convert to a web app using Flask/FastAPI
2. **Multiple Models**: Support switching between OpenAI and Ollama
3. **Conversation Analytics**: Analyze conversation patterns
4. **Plugin System**: Allow custom commands
5. **Multi-user Support**: Track different users
6. **Search**: Search through conversation history

## Reflection Questions

After completing the project:
1. What was the hardest part of the setup?
2. How did context management improve the chatbot?
3. What features would you add next?
4. How does this compare to the basic chatbot?
5. What professional practices did you learn?

## Next Steps

After completing this project:
- Review your project structure
- Consider adding tests
- Experiment with different system prompts
- Prepare for Chapter 4 (AI capabilities and limitations)

---

**Remember**: This project is about professional practices as much as functionality. Focus on doing things the "right way."

