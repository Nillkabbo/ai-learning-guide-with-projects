# Chapter 5 Project: E-Commerce Recommendation Assistant

## Project Overview

Build a complete e-commerce recommendation assistant that uses system messages, conversation history, function calling, and streaming to provide personalized product recommendations. This project demonstrates all major OpenAI API features in a practical application.

## Learning Objectives

By completing this project, you will:
- Use system messages to create a shopping assistant personality
- Manage conversation history for context-aware recommendations
- Implement function calling to search products
- Use streaming for real-time responses
- Build a complete, production-ready application

## Project Type

**Cumulative** - Builds on Chapters 1-4, demonstrates all Chapter 5 concepts.

## Prerequisites

- Completed Chapter 5
- OpenAI API key (or Ollama installed)
- Understanding of function calling
- Basic Python OOP knowledge

## Project Requirements

### Core Features (Must Have)

1. **Shopping Assistant Personality**
   - System message defining assistant role
   - Friendly, helpful shopping expert
   - Product knowledge and recommendations

2. **Conversation Management**
   - Maintain conversation history
   - Context-aware recommendations
   - Multi-turn conversations

3. **Product Search Function**
   - Function calling for product search
   - Search by category, price, features
   - Return product recommendations

4. **Streaming Responses**
   - Real-time response display
   - Better user experience
   - Progress indication

5. **Interactive Interface**
   - Command-line interface
   - User-friendly prompts
   - Clear product displays

### Extended Features (Nice to Have)

- Product comparison
- Price alerts
- Wishlist management
- Search history
- Multiple product categories
- Image analysis (if using vision models)

## Step-by-Step Instructions

### Step 1: Basic Structure

**Checkpoint 1**: Can you create the basic chatbot?

1. Create ShoppingAssistant class
2. Initialize with system message
3. Implement basic chat method
4. Test with simple queries

### Step 2: Conversation History

**Checkpoint 2**: Does the assistant remember context?

1. Add conversation history management
2. Test multi-turn conversations
3. Verify context retention
4. Handle conversation reset

### Step 3: Product Search Function

**Checkpoint 3**: Can the assistant search products?

1. Create product database (mock or real)
2. Define search function
3. Implement function calling
4. Test product recommendations

### Step 4: Streaming

**Checkpoint 4**: Are responses streamed?

1. Implement streaming
2. Display tokens as they arrive
3. Improve user experience
4. Handle streaming errors

### Step 5: Integration

**Checkpoint 5**: Does everything work together?

1. Combine all features
2. Polish user interface
3. Add error handling
4. Test complete flow

## Project Milestones

### Milestone 1: Basic Assistant (1 hour)
- [ ] ShoppingAssistant class created
- [ ] System message implemented
- [ ] Basic chat working

### Milestone 2: Conversation (45 minutes)
- [ ] History management
- [ ] Context retention
- [ ] Multi-turn conversations

### Milestone 3: Function Calling (1.5 hours)
- [ ] Product search function
- [ ] Function calling implemented
- [ ] Recommendations working

### Milestone 4: Streaming (45 minutes)
- [ ] Streaming implemented
- [ ] Real-time display
- [ ] UX improvements

### Milestone 5: Polish (1 hour)
- [ ] Error handling
- [ ] User interface
- [ ] Documentation

## Example Usage

```
$ python shopping_assistant.py

🛍️  E-Commerce Recommendation Assistant
Type 'quit' to exit

You: I'm looking for a wireless mouse under $50

Assistant: [streaming] I'd be happy to help you find a wireless mouse under $50! Let me search our product catalog...

[Function called: search_products(category="mouse", max_price=50)]

Assistant: [streaming] I found several great options! Here are my top recommendations:

1. Logitech M705 - $39.99
   - Wireless, ergonomic design, long battery life
   - Perfect for office use

2. Microsoft Surface Mouse - $34.99
   - Sleek design, Bluetooth connectivity
   - Great for travel

Would you like more details on any of these?

You: Tell me more about the Logitech one

Assistant: [streaming] The Logitech M705 is an excellent choice! Here are the key features...
```

## Success Criteria

Your project is successful if:
- ✅ System message creates shopping personality
- ✅ Conversation history works correctly
- ✅ Function calling finds products
- ✅ Streaming provides real-time feedback
- ✅ Complete user experience is smooth
- ✅ Code is well-organized and documented

## Extension Ideas

1. **Multiple Categories**: Expand beyond electronics
2. **Price Comparison**: Compare across retailers
3. **User Preferences**: Remember user preferences
4. **Image Analysis**: Use vision to analyze product images
5. **Voice Interface**: Add text-to-speech
6. **Web Interface**: Convert to web app

## Next Steps

After completing this project:
- Review function calling patterns
- Experiment with different system messages
- Try adding more functions
- Prepare for Chapter 6 (Claude API)

---

**Remember**: This project combines all Chapter 5 concepts. Take it step by step and master each component before combining them.
