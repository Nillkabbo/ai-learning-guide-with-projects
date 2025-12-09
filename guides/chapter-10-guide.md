# Chapter 10 Learning Guide: Advanced Prompting Strategies

## Overview

This chapter covers advanced prompting strategies for complex problems: self-consistency, tree-of-thought, ReAct, multi-agent debate, and reflexion. These are structured, multi-step reasoning frameworks for tackling complexity.


## Navigation

**← Previous**: [Chapter 9: Fundamental Prompt Engineering](chapter-09-guide.md)

**Next →**: [Chapter 11: Structured Output Generation](chapter-11-guide.md)

## Educator Perspective

### Teaching Strategy

**Key Concepts to Emphasize:**
1. Self-consistency: multiple runs, find consensus
2. Tree-of-thought: explore multiple reasoning paths
3. ReAct: reasoning + acting in loops
4. Multi-agent debate: multiple perspectives
5. Reflexion: self-improving agents

**Common Student Struggles:**
- **"Why run multiple times?"**: Show accuracy improvements
- **"Tree-of-thought seems complex"**: Start with simple trees
- **"ReAct loop is confusing"**: Break into steps
- **"Multi-agent is expensive"**: Explain when worth it

**Teaching Sequence:**
1. Self-consistency
2. Tree-of-thought
3. ReAct
4. Multi-agent debate
5. Reflexion
6. Complex problem solving

**Pacing:**
- This chapter should take 4-5 hours
- Emphasize when to use each strategy
- Build examples together
- Compare strategies

## Learner Perspective

### Prerequisites Check

- [ ] Completed Chapter 9 (fundamental prompting)
- [ ] Understand few-shot and chain-of-thought
- [ ] Can make multiple API calls
- [ ] Basic understanding of agents

### Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Implement self-consistency
- [ ] Use tree-of-thought for complex problems
- [ ] Build ReAct agents
- [ ] Create multi-agent debates
- [ ] Implement reflexion
- [ ] Choose appropriate strategy

## Section-by-Section Breakdown

### Section 1: Self-Consistency Method

**Key Concepts:**
- Run prompt multiple times
- Higher temperature for diversity
- Find most common answer
- Improves accuracy on single-answer tasks

**Learning Objectives:**
- Implement self-consistency
- Choose number of runs
- Analyze consensus
- Measure improvements

**Practice Exercises:**
1. Basic self-consistency
2. Test on math problems
3. Compare with single run
4. Optimize number of runs

---

### Section 2: Tree-of-Thought (ToT)

**Key Concepts:**
- Explore multiple reasoning paths
- Evaluate each path
- Choose best path
- Backtrack if needed

**Learning Objectives:**
- Implement ToT
- Design reasoning trees
- Evaluate paths
- Handle backtracking

**Practice Exercises:**
1. Simple ToT implementation
2. Complex problem solving
3. Path evaluation
4. Optimization

---

### Section 3: ReAct (Reasoning and Acting)

**Key Concepts:**
- Reasoning step
- Action step
- Observation step
- Loop until goal

**Learning Objectives:**
- Implement ReAct loop
- Design reasoning steps
- Choose actions
- Handle observations

**Practice Exercises:**
1. Basic ReAct agent
2. Multi-step problem solving
3. Tool integration
4. Complex scenarios

---

### Section 4: Multi-Agent Debate

**Key Concepts:**
- Multiple AI agents
- Different perspectives
- Debate and consensus
- Robust decisions

**Learning Objectives:**
- Create multiple agents
- Facilitate debate
- Reach consensus
- Measure improvements

**Practice Exercises:**
1. Two-agent debate
2. Multi-agent system
3. Consensus mechanisms
4. Complex decisions

---

### Section 5: Reflexion

**Key Concepts:**
- Self-reflection
- Learn from mistakes
- Improve reasoning
- Iterative refinement

**Learning Objectives:**
- Implement reflexion
- Design reflection prompts
- Learn from errors
- Improve over time

**Practice Exercises:**
1. Basic reflexion
2. Error learning
3. Iterative improvement
4. Complex problems

## Project Integration

### Chapter 10 Project: Advanced Problem Solver

**How the Project Reinforces Learning:**
- Uses all advanced strategies
- Compares approaches
- Solves complex problems
- Demonstrates when to use each

**Project Milestones:**
1. Self-consistency (1 hour)
2. Tree-of-thought (1.5 hours)
3. ReAct (1.5 hours)
4. Multi-agent (1.5 hours)
5. Reflexion (1 hour)
6. Complete system (1.5 hours)

## Study Schedule Recommendation

**For Complete Beginners:**
- Day 1: Sections 1-2 (2.5 hours)
- Day 2: Sections 3-4 (2.5 hours)
- Day 3: Section 5 (1.5 hours)
- Day 4: Project work (4 hours)

**For Experienced Programmers:**
- Session 1: Strategies overview (2 hours)
- Session 2: Implementation (3 hours)
- Session 3: Project (3 hours)
- Total: 8 hours

## Common Questions and Answers

**Q: When to use self-consistency?**
A: For single-answer tasks where accuracy matters (math, logic).

**Q: Is tree-of-thought worth the cost?**
A: For very complex problems where exploration helps.

**Q: ReAct vs. simple agents?**
A: ReAct for dynamic information gathering, simple agents for static tasks.

**Q: How many agents for debate?**
A: Start with 2-3, add more for complex decisions.

## Next Chapter Preview

Chapter 11 covers structured output generation - forcing AI into reliable formats.
---

## Navigation

**← Previous**: [Chapter 9: Fundamental Prompt Engineering](chapter-09-guide.md)

**Next →**: [Chapter 11: Structured Output Generation](chapter-11-guide.md)

