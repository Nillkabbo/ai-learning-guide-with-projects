# Chapter 2 Project: Smart IoT Troubleshooting Assistant

## Project Overview

Build an intelligent troubleshooting assistant that uses semantic search to find relevant solutions from a knowledge base. This project combines all three key concepts from Chapter 2: token counting for cost management, embeddings for semantic search, and context window management for conversations.

## Learning Objectives

By completing this project, you will:
- Count tokens and estimate API costs
- Create and compare embeddings
- Implement semantic search using embeddings
- Manage context windows for multi-turn conversations
- Build a practical AI application that uses all three concepts

## Project Type

**Cumulative** - This project builds on Chapter 1's IoT dashboard and will be extended in future chapters. It demonstrates how tokens, embeddings, and context work together in a real application.

## Prerequisites

- Completed Chapter 1 project
- Understanding of tokens, embeddings, and context windows
- Python 3.8+ with numpy installed
- OpenAI API key (or Ollama with embedding model)

## Project Requirements

### Core Features (Must Have)

1. **Token Counting and Cost Estimation**
   - Count tokens in user queries
   - Estimate API costs before making calls
   - Display token usage information

2. **Semantic Search**
   - Create embeddings for a knowledge base of troubleshooting solutions
   - Use semantic search to find most relevant solutions
   - Display similarity scores

3. **Context Management**
   - Track conversation history
   - Manage context window size
   - Implement sliding window when limit approached

4. **Troubleshooting Assistant**
   - Accept user problem descriptions
   - Find relevant solutions using semantic search
   - Maintain conversation context
   - Provide helpful, contextual responses

### Extended Features (Nice to Have)

- Cache embeddings to avoid recalculating
- Support multiple knowledge bases
- Visualize token usage over time
- Export conversation history
- Batch processing of problems
- Confidence scores for solutions

## Project Structure

```
chapter-02-project/
├── README.md
├── requirements.txt
├── starter-code/
│   └── troubleshooting_assistant.py
├── solution/
│   └── smart_troubleshooting.py
├── tests/
│   └── test_assistant.py
└── docs/
    └── knowledge_base.md
```

## Step-by-Step Instructions

### Step 1: Set Up Knowledge Base

Create a knowledge base of IoT troubleshooting solutions:

```python
# knowledge_base.py
TROUBLESHOOTING_SOLUTIONS = [
    "Check for direct sunlight hitting the sensor, as this can cause false high temperature readings.",
    "Restart the device's WiFi router if connectivity issues persist.",
    "Recalibrate the sensor against a known temperature source to ensure accuracy.",
    "Replace the device's battery if power levels drop below 10%.",
    "Check for physical obstructions blocking the sensor's detection area.",
    "Verify the device firmware is up to date for optimal performance.",
    "Inspect wiring connections for loose or corroded contacts.",
    "Reset the device to factory settings if all else fails.",
    # Add more solutions...
]
```

### Step 2: Implement Token Counting

**Checkpoint 1**: Can you count tokens and estimate costs?

```python
import tiktoken

def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    """Count tokens in text."""
    # TODO: Implement token counting
    pass

def estimate_cost(text: str, is_input: bool = True) -> float:
    """Estimate API cost for text."""
    # TODO: Calculate cost based on token count
    pass
```

### Step 3: Create Embeddings

**Checkpoint 2**: Can you create embeddings for the knowledge base?

```python
def create_knowledge_base_embeddings(solutions: list[str]) -> list[list[float]]:
    """Create embeddings for all solutions in knowledge base."""
    # TODO: Create embeddings for each solution
    # TODO: Store embeddings for reuse
    pass
```

### Step 4: Implement Semantic Search

**Checkpoint 3**: Can you find the most relevant solution?

```python
def find_best_solution(user_problem: str, solutions: list[str], embeddings: list[list[float]]) -> tuple[str, float]:
    """Find most relevant solution using semantic search."""
    # TODO: Create embedding for user problem
    # TODO: Compare with knowledge base embeddings
    # TODO: Return best match with similarity score
    pass
```

### Step 5: Add Context Management

**Checkpoint 4**: Can you manage conversation context?

```python
def manage_context(messages: list[dict], max_tokens: int = 120000) -> list[dict]:
    """Manage conversation context to stay within token limit."""
    # TODO: Keep system message
    # TODO: Remove oldest messages if needed
    # TODO: Return managed message list
    pass
```

### Step 6: Build the Complete Assistant

**Checkpoint 5**: Does everything work together?

Combine all components:
- Accept user problems
- Count tokens and estimate costs
- Use semantic search to find solutions
- Maintain conversation context
- Provide helpful responses

## Project Milestones

### Milestone 1: Token Counting (30 minutes)
- [ ] Can count tokens in text
- [ ] Can estimate costs
- [ ] Displays token information

### Milestone 2: Embeddings (45 minutes)
- [ ] Can create embeddings
- [ ] Stores embeddings efficiently
- [ ] Can compare embeddings

### Milestone 3: Semantic Search (45 minutes)
- [ ] Finds most relevant solution
- [ ] Returns similarity scores
- [ ] Handles edge cases

### Milestone 4: Context Management (30 minutes)
- [ ] Tracks conversation history
- [ ] Manages context window
- [ ] Preserves important messages

### Milestone 5: Complete Assistant (1 hour)
- [ ] All components integrated
- [ ] User interface works
- [ ] Handles errors gracefully
- [ ] Code is clean and documented

## Example Usage

```
$ python smart_troubleshooting.py

Smart IoT Troubleshooting Assistant
====================================
Knowledge base loaded: 20 solutions
Enter your IoT problem (type 'quit' to exit)

> My temperature sensor is reading way too high, like 95 degrees!

Tokens used: 15
Estimated cost: $0.000002
Searching knowledge base...

Found solution (similarity: 0.87):
"Check for direct sunlight hitting the sensor, as this can cause 
false high temperature readings."

Would you like more details? (y/n): y

[AI provides detailed explanation using the solution]

> The device keeps disconnecting from WiFi

Tokens used: 12
Estimated cost: $0.000002
Searching knowledge base...

Found solution (similarity: 0.82):
"Restart the device's WiFi router if connectivity issues persist."

> quit
Goodbye! Total tokens used: 150, Total cost: $0.000023
```

## Testing Your Project

### Test Cases

1. **Token Counting**
   - Short text (10 tokens)
   - Medium text (100 tokens)
   - Long text (1000 tokens)
   - Verify cost calculations

2. **Semantic Search**
   - Exact match (should find perfect solution)
   - Partial match (should find related solution)
   - No match (should handle gracefully)
   - Similarity scores are reasonable (0-1 range)

3. **Context Management**
   - Short conversation (no trimming needed)
   - Medium conversation (some trimming)
   - Long conversation (aggressive trimming)
   - System message always preserved

### What to Check

- Are token counts accurate?
- Do cost estimates match actual costs?
- Does semantic search find relevant solutions?
- Are similarity scores meaningful?
- Does context management work correctly?
- Does the assistant provide helpful responses?

## Success Criteria

Your project is successful if:
- ✅ Token counting works accurately
- ✅ Cost estimation is reasonable
- ✅ Semantic search finds relevant solutions
- ✅ Context management prevents overflow
- ✅ Assistant provides helpful troubleshooting advice
- ✅ Code is readable and well-commented
- ✅ You can explain how each component works

## Common Challenges and Solutions

**Challenge**: "Token counting seems wrong"
- **Solution**: Make sure you're using the correct encoder for your model

**Challenge**: "Embeddings are too slow"
- **Solution**: Cache embeddings, don't recreate them every time

**Challenge**: "Semantic search doesn't find good matches"
- **Solution**: Improve your knowledge base, check normalization, verify similarity calculation

**Challenge**: "Context management is confusing"
- **Solution**: Start simple—just remove oldest messages. Add sophistication later.

**Challenge**: "I don't understand cosine similarity"
- **Solution**: You don't need to—just know that higher scores = more similar. The libraries handle the math.

## Extension Ideas

1. **Embedding Cache**: Save embeddings to file to avoid recalculating
2. **Multiple Knowledge Bases**: Support different device types
3. **Visualization**: Graph token usage over time
4. **Batch Mode**: Process multiple problems at once
5. **Learning Mode**: Add new solutions based on user feedback
6. **Confidence Thresholds**: Only show solutions above a certain similarity

## Knowledge Base Suggestions

Create solutions for:
- Temperature sensor issues
- Humidity sensor problems
- Connectivity problems
- Power/battery issues
- Calibration needs
- Firmware updates
- Physical damage
- Environmental factors

## Reflection Questions

After completing the project:
1. How did token counting help you understand costs?
2. What surprised you about semantic search?
3. How did context management affect conversations?
4. What would you improve in your implementation?
5. How would you scale this to handle more solutions?

## Next Steps

After completing this project:
- Review token optimization techniques
- Experiment with different embedding models
- Test context management with very long conversations
- Prepare for Chapter 3 (development environment)

---

**Remember**: This project combines three complex concepts. Take it step by step. Master each component before combining them.

