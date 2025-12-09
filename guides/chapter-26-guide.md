# Chapter 26 Learning Guide: Fine-Tuning and Custom Models

## Overview

This chapter covers fine-tuning custom AI models on your data. You'll learn when to fine-tune vs. prompt engineering vs. RAG, data preparation, fine-tuning workflow, model evaluation, and deploying custom models.

## Educator Perspective

### Teaching Strategy

**Key Concepts to Emphasize:**
1. Fine-tuning is for skills, not facts
2. When to fine-tune (vs. prompting vs. RAG)
3. Data quality is critical (80% of work)
4. JSONL format for training data
5. Evaluation and deployment

**Common Student Struggles:**
- **"When should I fine-tune?"**: Show decision framework
- **"Data preparation is hard"**: Emphasize quality over quantity
- **"Fine-tuning seems expensive"**: Show when it's worth it
- **"How much data?"**: 50-100 high-quality examples often enough

**Teaching Sequence:**
1. When to fine-tune (decision framework)
2. Data preparation
3. Fine-tuning workflow
4. Model evaluation
5. Deployment
6. Complete system

**Pacing:**
- This chapter should take 4-5 hours
- Emphasize data quality
- Build IoT diagnostic assistant
- Evaluate results

## Learner Perspective

### Prerequisites Check

- [ ] Completed Chapters 1-25
- [ ] Understanding of prompting
- [ ] Knowledge of RAG (Chapter 27)
- [ ] Basic ML awareness

### Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Decide when to fine-tune
- [ ] Prepare high-quality datasets
- [ ] Execute fine-tuning jobs
- [ ] Evaluate custom models
- [ ] Deploy fine-tuned models
- [ ] Build specialized AI systems

## Section-by-Section Breakdown

### Section 1: When to Fine-Tune

**Key Concepts:**
- Fine-tuning vs. prompting
- Fine-tuning vs. RAG
- Decision framework
- Use cases
- When NOT to fine-tune

**Learning Objectives:**
- Understand tradeoffs
- Make informed decisions
- Choose right approach
- Avoid unnecessary fine-tuning

**Practice Exercises:**
1. Analyze use cases
2. Apply decision framework
3. Choose approach
4. Justify decisions

---

### Section 2: Data Preparation

**Key Concepts:**
- Quality over quantity
- JSONL format
- Message structure
- Consistency
- Clarity

**Learning Objectives:**
- Prepare datasets
- Format correctly
- Ensure quality
- Create examples

**Practice Exercises:**
1. Create dataset
2. Format JSONL
3. Ensure quality
4. Validate format

---

### Section 3: Fine-Tuning Workflow

**Key Concepts:**
- Upload training data
- Create fine-tuning job
- Monitor progress
- Wait for completion
- Retrieve model

**Learning Objectives:**
- Execute fine-tuning
- Monitor jobs
- Handle errors
- Complete workflow

**Practice Exercises:**
1. Upload data
2. Create job
3. Monitor progress
4. Retrieve model

---

### Section 4: Model Evaluation

**Key Concepts:**
- Compare to base model
- Test on validation set
- Measure improvements
- Quality assessment
- Cost-benefit analysis

**Learning Objectives:**
- Evaluate models
- Compare performance
- Measure improvements
- Make decisions

**Practice Exercises:**
1. Test fine-tuned model
2. Compare to base
3. Measure improvements
4. Assess value

---

### Section 5: Deployment

**Key Concepts:**
- Use fine-tuned model
- API integration
- Version management
- Cost considerations
- Monitoring

**Learning Objectives:**
- Deploy models
- Integrate with apps
- Manage versions
- Monitor usage

**Practice Exercises:**
1. Deploy model
2. Integrate with app
3. Test deployment
4. Monitor usage

## Project Integration

### Chapter 26 Project: Specialized IoT Diagnostic Assistant

**How the Project Reinforces Learning:**
- Implements fine-tuning workflow
- Prepares quality dataset
- Evaluates custom model
- Deploys fine-tuned model

**Project Milestones:**
1. Data preparation (2 hours)
2. Fine-tuning job (1 hour)
3. Model evaluation (1.5 hours)
4. Deployment (1.5 hours)
5. Complete system (2 hours)

## Study Schedule Recommendation

**For Complete Beginners:**
- Day 1: Sections 1-2 (2.5 hours)
- Day 2: Sections 3-4 (2.5 hours)
- Day 3: Section 5 (1.5 hours)
- Day 4: Project work (4 hours)

**For Experienced Programmers:**
- Session 1: Concepts (2 hours)
- Session 2: Implementation (3 hours)
- Session 3: Project (3 hours)
- Total: 8 hours

## Common Questions and Answers

**Q: When should I fine-tune?**
A: When you need to teach a new skill, style, or format that prompting can't achieve.

**Q: How much data do I need?**
A: 50-100 high-quality examples often enough. Quality over quantity.

**Q: Is fine-tuning expensive?**
A: Yes, but worth it for specialized tasks. Consider cost vs. value.

**Q: Can I fine-tune for facts?**
A: No, use RAG for factual knowledge. Fine-tuning is for skills.

## Next Chapter Preview

Chapter 27 covers RAG (Retrieval-Augmented Generation) - teaching AI new knowledge through retrieval.
