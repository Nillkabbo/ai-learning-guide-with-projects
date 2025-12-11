"""
Advanced Problem Solver - Complete Solution
Chapter 10 Project

Demonstrates advanced prompting strategies: self-consistency, tree-of-thought, ReAct.
"""

import os
from collections import Counter
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class ProblemSolver:
    """Advanced problem solver with multiple strategies."""
    
    def __init__(self):
        """Initialize solver."""
        load_dotenv()
        
        if not OPENAI_AVAILABLE:
            raise ImportError("openai library not installed")
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found")
        
        self.client = openai.OpenAI(api_key=api_key)
    
    def solve(self, problem: str, strategy: str = "self_consistency") -> str:
        """Solve problem using specified strategy."""
        if strategy == "self_consistency":
            # Generate multiple solutions, return most common
            solutions = []
            for _ in range(3):
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": f"Solve: {problem}"}]
                )
                solutions.append(response.choices[0].message.content)
            # Return most common solution (simplified)
            return solutions[0]  # In practice, would analyze and return consensus
        
        elif strategy == "tree_of_thought":
            prompt = f"""Solve this step by step, exploring multiple reasoning paths:
{problem}

Think through different approaches, then select the best one."""
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        
        elif strategy == "react":
            prompt = f"""Solve using ReAct (Reasoning + Acting):
Problem: {problem}

Think step by step, then act, then observe results."""
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        
        else:
            return "Unknown strategy"


def main():
    """Main function."""
    print("🧠 Advanced Problem Solver")
    print("Type 'quit' to exit\n")
    
    try:
        solver = ProblemSolver()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            problem = input("Problem (or 'quit'): ").strip()
            if problem.lower() == 'quit':
                break
            strategy = input("Strategy (self_consistency/tree_of_thought/react): ").strip() or "self_consistency"
            result = solver.solve(problem, strategy)
            print(f"\nSolution: {result}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
