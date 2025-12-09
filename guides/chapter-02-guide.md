# Chapter 2 Learning Guide: Tokens, Embeddings, and Context Windows

## Overview

This chapter dives into the "engine room" of AI—the fundamental mechanics that govern how LLMs work. Understanding tokens, embeddings, and context windows is essential for building cost-effective and efficient AI applications. These concepts might seem abstract, but they directly impact every application you'll build.

## Educator Perspective

### Teaching Strategy

**Key Concepts to Emphasize:**
1. Tokens = currency (cost directly tied to token count)
2. Embeddings = meaning (semantic understanding through vectors)
3. Context windows = memory (finite and must be managed)
4. All three concepts are interconnected and practical

**Common Student Struggles:**
- **"Tokens are confusing"**: Use the analogy—tokens are like "words" but not exactly words. Show examples.
- **"Embeddings are too abstract"**: Use the map analogy—cities close on a map are like words with similar meanings in embedding space.
- **"Why do I need to manage context?"**: Show what happens when context overflows—AI forgets earlier messages.
- **"Math is scary"**: Keep it simple—you don't need to calculate embeddings yourself, just understand the concept.

**Teaching Sequence:**
1. Tokens first (most concrete, directly affects cost)
2. Embeddings second (more abstract but powerful)
3. Context windows last (builds on token understanding)
4. Show practical applications throughout

**Pacing:**
- This chapter should take 3-4 hours for complete beginners
- Allow time for hands-on token counting
- Embedding examples need time to sink in
- Context management is practical but can be tricky

**Assessment Strategies:**
- Can they count tokens in a text?
- Can they estimate costs?
- Do they understand what embeddings represent?
- Can they build a semantic search tool?
- Do they understand context window limits?

## Learner Perspective

### Prerequisites Check

Before starting, you should:
- [ ] Understand basic Python (variables, functions, lists, dictionaries)
- [ ] Have completed Chapter 1 (understand message structure)
- [ ] Know how to make basic AI API calls
- [ ] Understand basic math concepts (vectors, similarity)

**If you're missing prerequisites:**
- Review Chapter 1 if message structure is unclear
- Brush up on Python lists and dictionaries
- Don't worry about vector math—we'll explain what you need

### Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Explain what tokens are and why they matter
- [ ] Count tokens in text using tiktoken
- [ ] Estimate API costs based on token counts
- [ ] Understand what embeddings are and how they work
- [ ] Create embeddings for text
- [ ] Build a semantic search tool
- [ ] Understand context window limitations
- [ ] Implement basic context management

### Study Strategies

**For Visual Learners:**
- Draw diagrams of tokenization process
- Visualize embeddings as points in space
- Create diagrams of context window overflow
- Map out the semantic search process

**For Hands-On Learners:**
- Count tokens for many different texts
- Experiment with different embedding models
- Build the semantic search tool yourself
- Test context management with long conversations

**For Reading/Writing Learners:**
- Take detailed notes on each concept
- Write your own explanations
- Create a token cost calculator
- Document embedding dimensions for different models

**For Auditory Learners:**
- Explain concepts out loud
- Discuss with others
- Use analogies to remember concepts
- Teach the concepts to reinforce learning

## Section-by-Section Breakdown

### Section 1: Tokens - The Currency of Language Models

**Purpose:** Make students understand that AI doesn't see words—it sees tokens, and this directly affects cost.

**Key Concepts:**
- Tokens are chunks of text (words, parts of words, punctuation)
- Different models use different tokenizers
- Cost is per token (input + output)
- Token count ≠ word count
- Concise prompts save money

**Learning Objectives:**
- Define what a token is
- Count tokens in text
- Understand token-to-cost relationship
- Write cost-effective prompts

**Practice Exercises:**
1. Count tokens in 10 different sentences
2. Compare token counts to word counts
3. Rewrite a long prompt to be more concise
4. Calculate costs for different prompt lengths
5. Build a token cost calculator

**Common Pitfalls:**
- Assuming 1 token = 1 word (not true!)
- Not counting output tokens in cost estimates
- Writing unnecessarily long prompts
- Forgetting that different models tokenize differently

**Connection to Next Section:**
Tokens are how AI "sees" text. Embeddings are how AI "understands" text.

**Troubleshooting:**
- **"tiktoken not found"**: Run `pip install tiktoken`
- **"Wrong token count"**: Make sure you're using the right model's encoder
- **"Cost seems wrong"**: Remember to count both input and output tokens

---

### Section 2: Embeddings - How AI Understands Meaning

**Purpose:** Help students understand how AI represents meaning mathematically and how this enables semantic search.

**Key Concepts:**
- Embeddings = text converted to numbers (vectors)
- Similar meanings = similar vectors
- Embeddings capture semantic relationships
- Can compare embeddings to find similarity
- Different models produce different dimensions

**Learning Objectives:**
- Understand what embeddings represent
- Create embeddings for text
- Compare embeddings to find similarity
- Build semantic search applications

**Practice Exercises:**
1. Create embeddings for related words (cat, dog, kitten)
2. Create embeddings for unrelated words (car, planet)
3. Compare similarity scores
4. Build a simple semantic search
5. Experiment with different embedding models

**Common Pitfalls:**
- Thinking embeddings are just word counts
- Comparing embeddings from different models directly
- Not normalizing vectors for cosine similarity
- Overthinking the math—you don't need to calculate embeddings yourself

**Connection to Previous/Next:**
Builds on tokenization. Sets up for context windows (embeddings help understand what to keep/remove).

**Important Notes:**
- OpenAI embeddings: 1536 dimensions (text-embedding-3-small)
- Ollama embeddings: 768 dimensions (nomic-embed-text) or 384 (all-minilm)
- Cannot directly compare embeddings from different models
- Cosine similarity is the standard comparison method

---

### Section 3: Context Windows - The AI's Limited Memory

**Purpose:** Teach students about context limits and how to manage long conversations.

**Key Concepts:**
- Context window = maximum tokens AI can consider
- Everything (system, user, assistant messages) counts
- Exceeding limit = AI forgets earlier messages
- Different models have different limits
- Must manage context for long conversations

**Learning Objectives:**
- Understand context window limitations
- Know context sizes for popular models
- Implement basic context management
- Design systems that respect context limits

**Practice Exercises:**
1. Calculate token count for a long conversation
2. Identify when context would overflow
3. Implement sliding window context management
4. Test with conversations of varying lengths
5. Design a context management strategy

**Common Pitfalls:**
- Forgetting system messages count toward limit
- Not managing context in long conversations
- Removing important context too early
- Not testing with realistic conversation lengths

**Connection to Previous/Next:**
Uses token counting from Section 1. Essential for building real applications (Chapter 3+).

**Practical Tips:**
- Always keep system message
- Remove oldest messages first
- Consider summarizing instead of removing
- Monitor token usage in production

---

## Project Integration

### Chapter 2 Project: Smart IoT Troubleshooting Assistant

**How the Project Reinforces Learning:**
- Uses token counting for cost estimation
- Implements semantic search with embeddings
- Manages context for multi-turn conversations
- Combines all three concepts in one application

**Project Milestones:**
1. **Milestone 1**: Token counting and cost estimation
2. **Milestone 2**: Embedding creation and comparison
3. **Milestone 3**: Semantic search implementation
4. **Milestone 4**: Context management for conversations
5. **Milestone 5**: Complete troubleshooting assistant

**Success Criteria:**
- Can count tokens accurately
- Can estimate costs
- Semantic search finds relevant solutions
- Context management works for long conversations
- Application is functional and useful

## Study Schedule Recommendation

**For Complete Beginners:**
- Day 1: Section 1 - Tokens (2 hours) - Counting and cost
- Day 2: Section 2 - Embeddings (2 hours) - Understanding and creating
- Day 3: Section 3 - Context Windows (1.5 hours) - Limits and management
- Day 4: Project work (3 hours) - Build troubleshooting assistant
- Day 5: Review and practice (1 hour) - Solidify understanding

**For Experienced Programmers:**
- Session 1: Read all sections (1.5 hours)
- Session 2: Run all code examples (1.5 hours)
- Session 3: Build project (2 hours)
- Total: 5 hours

## Common Questions and Answers

**Q: Do I need to understand vector math?**
A: No. You just need to understand the concept—similar meanings = similar vectors. The libraries handle the math.

**Q: Why are tokens different from words?**
A: Tokenization is more efficient—common words might be one token, rare words might be multiple tokens. It's optimized for the model.

**Q: Can I use embeddings from different models together?**
A: No. Different models produce different dimensions and meanings. Stick to one model per application.

**Q: What happens if I exceed the context window?**
A: The API will either error or truncate. Always manage context proactively.

**Q: How do I choose an embedding model?**
A: For OpenAI, use text-embedding-3-small (good balance). For Ollama, use nomic-embed-text (768 dims) or all-minilm (384 dims, faster).

## Additional Resources

- tiktoken Documentation: https://github.com/openai/tiktoken
- OpenAI Embeddings Guide: https://platform.openai.com/docs/guides/embeddings
- Vector Similarity Explained: https://www.pinecone.io/learn/vector-similarity/
- Context Window Management: Best practices for managing long conversations

## Next Chapter Preview

Chapter 3 will cover:
- Setting up a professional development environment
- Project structure and organization
- Building a command-line chatbot
- This builds on context management from Chapter 2

