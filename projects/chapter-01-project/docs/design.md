# IoT Device Status Dashboard - Design Document

## Overview

The IoT Device Status Dashboard is a command-line tool that uses AI to interpret and explain IoT device status messages in plain English. This project demonstrates the fundamental concepts of AI engineering: making API calls, using message roles, and building practical applications.

## Architecture

### Components

1. **AI Integration Module**
   - Handles communication with AI models (OpenAI or Ollama)
   - Manages message structure (system, user, assistant)
   - Processes API responses

2. **User Interface Module**
   - Command-line input/output
   - Message formatting
   - Error handling

3. **Main Application**
   - Orchestrates components
   - Manages application flow
   - Handles user interaction loop

## Design Decisions

### Why Command-Line Interface?

- Simple to implement
- Focuses on core AI concepts
- Easy to test and debug
- No additional dependencies

### Why Support Both OpenAI and Ollama?

- Demonstrates flexibility
- Allows offline development
- Shows API abstraction
- Provides cost/privacy options

### Message Structure

- **System Message**: Sets AI's role as IoT expert
- **User Message**: Contains device status to interpret
- **Assistant Message**: (Future) Could maintain conversation context

## Extension Ideas

1. **Multi-Device Support**: Handle different device types with specialized interpreters
2. **Severity Detection**: Automatically classify message severity
3. **History**: Save interpretations to a file
4. **Batch Mode**: Process multiple messages from a file
5. **Web Interface**: Convert to Flask/FastAPI web app
6. **Color Coding**: Use terminal colors for different status types

## Future Enhancements

- Conversation history for follow-up questions
- Device-specific knowledge bases
- Integration with actual IoT systems
- Real-time monitoring mode
- Alert system for critical statuses
