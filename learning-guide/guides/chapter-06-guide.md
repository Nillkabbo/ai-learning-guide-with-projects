# Chapter 6 Learning Guide: Mastering the Anthropic Claude API

## Overview

This chapter introduces the Anthropic Claude API as an alternative to OpenAI. Claude is known for strong reasoning, large context windows, and focus on helpful, harmless, honest AI. You'll learn Claude's API structure, system prompts, document analysis, tool use, and vision capabilities.


## Navigation

**← Previous**: [Chapter 5: OpenAI API Complete Guide](chapter-05-guide.md)

**Next →**: [Chapter 7: Google Gemini API Guide](chapter-07-guide.md)

## Educator Perspective

### Teaching Strategy

**Key Concepts to Emphasize:**
1. Claude API differences from OpenAI
2. Dedicated system parameter (more reliable)
3. Large context windows (200K tokens)
4. Tool use (similar to function calling)
5. Vision capabilities
6. Model selection (Sonnet, Opus, Haiku)

**Common Student Struggles:**
- **"API structure is different"**: Show side-by-side comparisons
- **"max_tokens is required"**: Emphasize this difference
- **"Response structure differs"**: Demonstrate extraction patterns
- **"When to use Claude vs OpenAI?"**: Compare strengths

**Teaching Sequence:**
1. Basic Claude API call
2. System prompts (dedicated parameter)
3. Conversation management
4. Long document analysis
5. Tool use
6. Vision capabilities

**Pacing:**
- This chapter should take 3-4 hours
- Compare with OpenAI throughout
- Emphasize Claude's strengths
- Build IoT fleet management project

## Learner Perspective

### Prerequisites Check

- [ ] Completed Chapter 5 (OpenAI API)
- [ ] Understand API basics
- [ ] Have Anthropic API key
- [ ] Understand function calling concepts

### Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Make Claude API calls
- [ ] Use dedicated system parameter
- [ ] Analyze long documents
- [ ] Implement tool use
- [ ] Use vision capabilities
- [ ] Choose appropriate Claude models

## Section-by-Section Breakdown

### Section 1: Your First Claude API Call

**Key Concepts:**
- `anthropic.Anthropic()` client
- `client.messages.create()` method
- `max_tokens` is required
- Response: `message.content[0].text`
- Model names: `claude-3-5-sonnet-20240620`

**Learning Objectives:**
- Make basic Claude call
- Understand API differences
- Extract responses correctly

**Practice Exercises:**
1. Make "Hello, Claude!" call
2. Compare with OpenAI structure
3. Create reusable function
4. Handle errors

---

### Section 2: System Prompts

**Key Concepts:**
- Dedicated `system` parameter (not in messages)
- More reliable adherence
- Better personality control
- Detailed instructions work well

**Learning Objectives:**
- Use system parameter effectively
- Create detailed system prompts
- Compare with OpenAI approach

**Practice Exercises:**
1. Create IoT expert persona
2. Test detailed instructions
3. Compare adherence
4. Experiment with personas

---

### Section 3: Long Document Analysis

**Key Concepts:**
- Large context windows (200K tokens)
- Document analysis capabilities
- Conversation with documents
- Context management

**Learning Objectives:**
- Analyze long documents
- Build document Q&A systems
- Manage large contexts
- Leverage Claude's strengths

**Practice Exercises:**
1. Build DocumentAnalyzerBot
2. Analyze technical documents
3. Answer questions from context
4. Test context limits

---

### Section 4: Tool Use

**Key Concepts:**
- Similar to OpenAI function calling
- Tool descriptions
- Tool execution
- Result feedback

**Learning Objectives:**
- Implement tool use
- Describe tools to Claude
- Execute tools safely
- Handle tool results

**Practice Exercises:**
1. Create tool registry
2. Implement tool calling
3. Build tool-using agent
4. Test tool execution

---

### Section 5: Vision Capabilities

**Key Concepts:**
- Image analysis
- Base64 encoding
- Vision models
- Multimodal prompts

**Learning Objectives:**
- Analyze images with Claude
- Use vision for diagnostics
- Combine text and images
- Understand limitations

**Practice Exercises:**
1. Analyze device images
2. Visual diagnostics
3. Combine modalities
4. Build vision applications

## Project Integration

### Chapter 6 Project: IoT Fleet Management System

**How the Project Reinforces Learning:**
- Uses Claude's system prompts
- Analyzes device data (long context)
- Implements tool use for device control
- Uses vision for diagnostics
- Demonstrates Claude's strengths

**Project Milestones:**
1. Basic Claude integration
2. System prompt for fleet manager
3. Document analysis for device logs
4. Tool use for device actions
5. Vision for diagnostics
6. Complete system

## Study Schedule Recommendation

**For Complete Beginners:**
- Day 1: Sections 1-2 (2 hours) - Basics and system prompts
- Day 2: Sections 3-4 (2 hours) - Documents and tools
- Day 3: Section 5 (1 hour) - Vision
- Day 4: Project work (3 hours)

**For Experienced Programmers:**
- Session 1: Review API differences (1.5 hours)
- Session 2: Advanced features (1.5 hours)
- Session 3: Project (2 hours)
- Total: 5 hours

## Common Questions and Answers

**Q: When should I use Claude vs OpenAI?**
A: Claude for long documents, detailed instructions, reasoning. OpenAI for speed, cost, function calling.

**Q: Why is max_tokens required?**
A: Claude requires explicit limits for safety and cost control.

**Q: Are system prompts better in Claude?**
A: Yes, dedicated parameter often leads to better adherence.

**Q: Can I use both APIs?**
A: Yes! Many apps use multiple providers for different tasks.

## Next Chapter Preview

Chapter 7 covers Google Gemini API, completing the trio of major AI providers.
---

## Navigation

**← Previous**: [Chapter 5: OpenAI API Complete Guide](chapter-05-guide.md)

**Next →**: [Chapter 7: Google Gemini API Guide](chapter-07-guide.md)

