# Chapter 14 Learning Guide: Giving Your Agent Tools

## Overview

This chapter teaches tool use and function calling - giving agents the ability to interact with external systems. You'll learn the tool-use loop, implement function calling across providers, design tool schemas, build tool registries, and create secure execution environments.

## Educator Perspective

### Teaching Strategy

**Key Concepts to Emphasize:**
1. Two-step tool-use loop (AI decides → you execute)
2. Tool descriptions (JSON schemas)
3. Secure execution
4. Tool registries
5. Multi-step tool chains

**Common Student Struggles:**
- **"Tool-use loop is confusing"**: Break into clear steps
- **"Schema design is hard"**: Start simple, add detail
- **"Security concerns"**: Emphasize validation
- **"Ollama differences"**: Show prompt-based approach

**Teaching Sequence:**
1. Power of tools
2. Tool-use loop
3. Provider implementations
4. Tool schemas
5. Tool registries
6. Secure execution

**Pacing:**
- This chapter should take 4-5 hours
- Emphasize security
- Build tool system together
- Test tool execution

## Learner Perspective

### Prerequisites Check

- [ ] Completed Chapter 13 (agents)
- [ ] Understand function calling basics
- [ ] Can design JSON schemas
- [ ] Understanding of security

### Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Understand tool-use loop
- [ ] Implement function calling
- [ ] Design tool schemas
- [ ] Build tool registries
- [ ] Secure tool execution
- [ ] Chain tools together

## Section-by-Section Breakdown

### Section 1: Power of Tools

**Key Concepts:**
- Agents without tools are limited
- Tools enable actions
- Bridge to external systems
- Transform passive to active

**Learning Objectives:**
- Understand tool value
- See limitations without tools
- Recognize tool needs

**Practice Exercises:**
1. Build agent without tools
2. Identify limitations
3. Design needed tools
4. See tool value

---

### Section 2: Tool-Use Loop

**Key Concepts:**
- Step 1: AI decides to use tool
- Step 2: You execute tool
- Step 3: Send result back
- Step 4: AI uses result

**Learning Objectives:**
- Understand loop structure
- Implement loop
- Handle tool results
- Manage conversation

**Practice Exercises:**
1. Implement basic loop
2. Handle tool calls
3. Execute tools
4. Feed results back

---

### Section 3: Provider Implementations

**Key Concepts:**
- OpenAI: native function calling
- Claude: tool use
- Gemini: function calling
- Ollama: prompt-based

**Learning Objectives:**
- Implement for each provider
- Understand differences
- Choose approach
- Handle variations

**Practice Exercises:**
1. OpenAI function calling
2. Claude tool use
3. Gemini functions
4. Ollama prompt-based

---

### Section 4: Tool Schemas

**Key Concepts:**
- JSON schema format
- Parameter descriptions
- Type definitions
- Required fields

**Learning Objectives:**
- Design tool schemas
- Describe parameters
- Define types
- Validate schemas

**Practice Exercises:**
1. Create simple schema
2. Add parameters
3. Define types
4. Test schema

---

### Section 5: Tool Registries

**Key Concepts:**
- Centralized tool management
- Tool discovery
- Tool execution
- Tool security

**Learning Objectives:**
- Build tool registry
- Register tools
- Execute tools
- Manage tools

**Practice Exercises:**
1. Create registry
2. Register tools
3. Execute from registry
4. Add security

---

### Section 6: Secure Execution

**Key Concepts:**
- Input validation
- Permission checks
- Sandboxing
- Audit logging

**Learning Objectives:**
- Validate inputs
- Check permissions
- Secure execution
- Log actions

**Practice Exercises:**
1. Add input validation
2. Implement permissions
3. Secure execution
4. Add logging

## Project Integration

### Chapter 14 Project: Tool-Enabled IoT Agent

**How the Project Reinforces Learning:**
- Implements tool-use loop
- Uses tool registry
- Secures execution
- Chains tools together

**Project Milestones:**
1. Basic tool-use (1.5 hours)
2. Tool registry (1.5 hours)
3. Secure execution (1.5 hours)
4. Tool chains (1.5 hours)
5. Complete system (1.5 hours)

## Study Schedule Recommendation

**For Complete Beginners:**
- Day 1: Sections 1-2 (2.5 hours)
- Day 2: Sections 3-4 (2.5 hours)
- Day 3: Sections 5-6 (2.5 hours)
- Day 4: Project work (4 hours)

**For Experienced Programmers:**
- Session 1: Concepts (2 hours)
- Session 2: Implementation (3 hours)
- Session 3: Project (3 hours)
- Total: 8 hours

## Common Questions and Answers

**Q: How many tools should an agent have?**
A: Start with 2-5 essential tools, add more as needed.

**Q: How do I secure tool execution?**
A: Validate inputs, check permissions, sandbox if needed, log everything.

**Q: Ollama vs. OpenAI for tools?**
A: OpenAI native is easier, Ollama requires more prompt engineering.

**Q: Can tools call other tools?**
A: Yes, but be careful of loops and complexity.

## Next Chapter Preview

Chapter 15 covers building production-ready agents with frameworks, state management, and observability.
