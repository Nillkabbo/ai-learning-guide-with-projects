#!/usr/bin/env python3
"""
Add navigation links (Previous/Next chapter) to all learning guide files.
"""

import os
import re

def get_chapter_number(filename):
    """Extract chapter number from filename."""
    match = re.search(r'chapter-(\d+)-guide\.md', filename)
    return int(match.group(1)) if match else None

def get_navigation_links(chapter_num):
    """Generate navigation links for a chapter."""
    nav_top = "\n## Navigation\n\n"
    nav_bottom = "\n---\n\n## Navigation\n\n"
    
    if chapter_num == 1:
        nav_top += "**← Previous**: None (This is the first chapter)\n\n"
        nav_top += "**Next →**: [Chapter 2: Core Concepts](chapter-02-guide.md)\n\n"
        nav_bottom += "**← Previous**: None (This is the first chapter)\n\n"
        nav_bottom += "**Next →**: [Chapter 2: Core Concepts](chapter-02-guide.md)\n\n"
    elif chapter_num == 30:
        prev_num = f"{chapter_num - 1:02d}"
        nav_top += f"**← Previous**: [Chapter {chapter_num - 1}: Emerging Patterns and Future Trends](chapter-{prev_num}-guide.md)\n\n"
        nav_top += "**Next →**: None (This is the final chapter)\n\n"
        nav_bottom += f"**← Previous**: [Chapter {chapter_num - 1}: Emerging Patterns and Future Trends](chapter-{prev_num}-guide.md)\n\n"
        nav_bottom += "**Next →**: None (This is the final chapter)\n\n"
    else:
        prev_num = f"{chapter_num - 1:02d}"
        next_num = f"{chapter_num + 1:02d}"
        
        # Chapter titles for navigation
        chapter_titles = {
            1: "Welcome to AI Engineering",
            2: "Core Concepts",
            3: "Development Environment",
            4: "AI Capabilities & Limitations",
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
            30: "Building AI Products"
        }
        
        prev_title = chapter_titles.get(chapter_num - 1, f"Chapter {chapter_num - 1}")
        next_title = chapter_titles.get(chapter_num + 1, f"Chapter {chapter_num + 1}")
        
        nav_top += f"**← Previous**: [Chapter {chapter_num - 1}: {prev_title}](chapter-{prev_num}-guide.md)\n\n"
        nav_top += f"**Next →**: [Chapter {chapter_num + 1}: {next_title}](chapter-{next_num}-guide.md)\n\n"
        nav_bottom += f"**← Previous**: [Chapter {chapter_num - 1}: {prev_title}](chapter-{prev_num}-guide.md)\n\n"
        nav_bottom += f"**Next →**: [Chapter {chapter_num + 1}: {next_title}](chapter-{next_num}-guide.md)\n\n"
    
    return nav_top, nav_bottom

def add_navigation_to_file(filepath, chapter_num):
    """Add navigation links to a guide file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if navigation already exists
    if '## Navigation' in content:
        print(f"  ⚠️  Navigation already exists in {os.path.basename(filepath)}, skipping...")
        return False
    
    nav_top, nav_bottom = get_navigation_links(chapter_num)
    
    # Add navigation after the Overview section
    # Look for "## Overview" followed by content, then add nav after first paragraph or section
    overview_pattern = r'(## Overview\n\n.*?)(## )'
    match = re.search(overview_pattern, content, re.DOTALL)
    
    if match:
        # Insert navigation after Overview section, before next section
        content = content[:match.end(1)] + nav_top + match.group(2) + content[match.end():]
    else:
        # If no Overview section, add after title
        title_pattern = r'(# Chapter \d+.*?\n\n)'
        match = re.search(title_pattern, content)
        if match:
            content = content[:match.end()] + nav_top + content[match.end():]
    
    # Add navigation at the end
    # Remove trailing whitespace and add navigation
    content = content.rstrip() + nav_bottom
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    guides_dir = os.path.dirname(os.path.abspath(__file__)) + '/guides'
    
    if not os.path.exists(guides_dir):
        print(f"Error: {guides_dir} does not exist")
        return
    
    files = sorted([f for f in os.listdir(guides_dir) if f.startswith('chapter-') and f.endswith('-guide.md')])
    
    print(f"Processing {len(files)} guide files...")
    
    updated = 0
    skipped = 0
    
    for filename in files:
        chapter_num = get_chapter_number(filename)
        if chapter_num is None:
            print(f"  ⚠️  Could not extract chapter number from {filename}")
            continue
        
        filepath = os.path.join(guides_dir, filename)
        if add_navigation_to_file(filepath, chapter_num):
            print(f"  ✅ Added navigation to {filename}")
            updated += 1
        else:
            skipped += 1
    
    print(f"\n✅ Complete! Updated {updated} files, skipped {skipped} files (already had navigation)")

if __name__ == '__main__':
    main()

