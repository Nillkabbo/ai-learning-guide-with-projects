#!/usr/bin/env python3
"""
Script to generate learning guide materials for remaining chapters.
This creates template files that can be filled in with chapter-specific content.
"""

import os
from pathlib import Path

# Chapter titles mapping (update based on actual chapter files)
CHAPTER_TITLES = {
    5: "OpenAI API Complete Guide",
    6: "Anthropic Claude API Mastery",
    7: "Google Gemini API Guide",
    8: "API Design Patterns",
    9: "Fundamental Prompt Engineering",
    10: "Advanced Prompting Strategies",
    11: "Structured Output Generation",
    12: "Domain-Specific Prompting",
    13: "Introduction to AI Agents",
    14: "Tool Use and Function Calling",
    15: "Building Production Agents",
    16: "Multi-Agent Systems",
    17: "Building AI-Powered Web Applications",
    18: "Real-Time AI Applications",
    19: "AI Application Architecture Patterns",
    20: "Scaling AI Applications",
    21: "Cost Optimization",
    22: "Security and Safety",
    23: "Monitoring and Observability",
    24: "Testing AI Systems",
    25: "Deployment and DevOps",
    26: "Fine-Tuning Custom Models",
    27: "RAG (Retrieval Augmented Generation)",
    28: "AI Workflows and Orchestration",
    29: "Emerging Patterns and Future Trends",
    30: "Building AI Products",
}

BASE_DIR = Path(__file__).parent

def create_guide_template(chapter_num, title):
    """Create a learning guide template."""
    guide_path = BASE_DIR / "guides" / f"chapter-{chapter_num:02d}-guide.md"
    
    template = f"""# Chapter {chapter_num} Learning Guide: {title}

## Overview

[Brief overview of chapter content and importance]

## Educator Perspective

### Teaching Strategy

**Key Concepts to Emphasize:**
- [Concept 1]
- [Concept 2]
- [Concept 3]

**Common Student Struggles:**
- [Struggle 1 and solution]
- [Struggle 2 and solution]

**Teaching Sequence:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Pacing:**
- Estimated time: [X] hours

## Learner Perspective

### Prerequisites Check

- [ ] Completed previous chapters
- [ ] [Specific prerequisite]

### Learning Objectives

By the end of this chapter, you will be able to:
- [ ] [Objective 1]
- [ ] [Objective 2]
- [ ] [Objective 3]

## Section-by-Section Breakdown

[To be filled based on actual chapter content]

## Project Integration

### Chapter {chapter_num} Project: [Project Name]

**How the Project Reinforces Learning:**
- [How project applies concepts]

**Project Milestones:**
1. **Milestone 1**: [Description]
2. **Milestone 2**: [Description]

## Study Schedule Recommendation

**For Complete Beginners:**
- Day 1: [Sections] ([X] hours)
- Day 2: [Sections] ([X] hours)

**For Experienced Programmers:**
- Session 1: [Content] ([X] hours)
- Total: [X] hours

## Common Questions and Answers

**Q: [Question]**
A: [Answer]

## Next Chapter Preview

[What comes next]
"""
    
    guide_path.write_text(template)
    print(f"Created: {guide_path}")

def create_project_readme(chapter_num, title):
    """Create a project README template."""
    project_dir = BASE_DIR / "projects" / f"chapter-{chapter_num:02d}-project"
    readme_path = project_dir / "README.md"
    
    template = f"""# Chapter {chapter_num} Project: [Project Name]

## Project Overview

[Brief project description]

## Learning Objectives

By completing this project, you will:
- [Objective 1]
- [Objective 2]

## Project Type

**Standalone** or **Cumulative**

## Prerequisites

- Completed Chapter {chapter_num}
- [Additional prerequisites]

## Project Requirements

### Core Features (Must Have)

1. **[Feature 1]**
   - [Description]

2. **[Feature 2]**
   - [Description]

### Extended Features (Nice to Have)

- [Feature 1]
- [Feature 2]

## Step-by-Step Instructions

### Step 1: [Step Name]

**Checkpoint 1**: [Checkpoint description]

[Instructions]

## Project Milestones

### Milestone 1: [Name] ([X] minutes)
- [ ] [Task 1]
- [ ] [Task 2]

## Example Usage

```
[Example output]
```

## Success Criteria

Your project is successful if:
- ✅ [Criterion 1]
- ✅ [Criterion 2]

## Extension Ideas

1. [Idea 1]
2. [Idea 2]

## Next Steps

[What to do after completing]
"""
    
    readme_path.write_text(template)
    print(f"Created: {readme_path}")

def create_cursor_rules(chapter_num, title):
    """Create cursor rules template."""
    rules_path = BASE_DIR / ".cursorrules" / f"chapter-{chapter_num:02d}.cursorrules"
    
    template = f"""# Chapter {chapter_num}: {title} - Cursor Rules

## Chapter Context

[Brief context about what this chapter covers]

## Key Concepts

### 1. [Concept 1]
- [Detail 1]
- [Detail 2]

### 2. [Concept 2]
- [Detail 1]
- [Detail 2]

## Important Code Patterns

```python
# [Pattern description]
[Code example]
```

## Common Mistakes to Avoid

1. **[Mistake 1]**: [Why it's a mistake and how to avoid]

2. **[Mistake 2]**: [Why it's a mistake and how to avoid]

## Integration Points

### Prerequisites
- [Previous chapter concepts needed]

### Next Chapter Preparation
- [What this chapter prepares for]

## Project Context

### Chapter {chapter_num} Project: [Project Name]
- **Type**: [Standalone/Cumulative]
- **Focus**: [Main focus areas]
- **Key Skills**: [Skills developed]

## Related Chapters

- **Chapter X**: [Relationship]
- **Chapter Y**: [Relationship]
"""
    
    rules_path.write_text(template)
    print(f"Created: {rules_path}")

def main():
    """Generate templates for chapters 5-30."""
    print("Generating chapter materials...")
    
    for chapter_num in range(5, 31):
        title = CHAPTER_TITLES.get(chapter_num, f"Chapter {chapter_num}")
        print(f"\nChapter {chapter_num}: {title}")
        
        # Ensure directories exist
        (BASE_DIR / "guides").mkdir(exist_ok=True)
        (BASE_DIR / "projects" / f"chapter-{chapter_num:02d}-project").mkdir(exist_ok=True)
        (BASE_DIR / ".cursorrules").mkdir(exist_ok=True)
        
        # Create templates
        create_guide_template(chapter_num, title)
        create_project_readme(chapter_num, title)
        create_cursor_rules(chapter_num, title)
    
    print("\n✅ Template generation complete!")
    print("Next: Fill in chapter-specific content based on actual chapter files.")

if __name__ == "__main__":
    main()

