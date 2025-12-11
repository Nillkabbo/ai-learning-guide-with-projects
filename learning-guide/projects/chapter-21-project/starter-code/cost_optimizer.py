"""
Cost-Optimized AI System - Starter Code
Chapter 21 Project

This starter code provides a basic structure for building a cost-optimized
AI system with caching, batch processing, and model selection.
"""

import os
from typing import Dict, List
from collections import defaultdict

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai
# import tiktoken
# from cachetools import TTLCache


class CostOptimizer:
    """Cost-optimized AI system."""
    
    def __init__(self):
        """Initialize cost optimizer."""
        # TODO: Initialize OpenAI client
        # TODO: Initialize cache
        # TODO: Initialize token counter
        self.cost_tracker = defaultdict(float)
        self.usage_stats = defaultdict(int)
    
    def track_cost(self, tokens: int, model: str, is_input: bool = True) -> float:
        """
        Track and calculate cost.
        
        Args:
            tokens: Number of tokens
            model: Model name
            is_input: Whether tokens are input or output
            
        Returns:
            Cost in dollars
        """
        # TODO: Calculate cost based on model pricing
        # TODO: Track usage
        return 0.0
    
    def get_cached_response(self, prompt: str) -> str:
        """
        Get cached response if available.
        
        Args:
            prompt: User prompt
            
        Returns:
            Cached response or None
        """
        # TODO: Check cache
        # TODO: Return cached response if found
        return None
    
    def batch_process(self, prompts: List[str]) -> List[str]:
        """
        Process multiple prompts in batch.
        
        Args:
            prompts: List of prompts
            
        Returns:
            List of responses
        """
        # TODO: Implement batch processing
        # TODO: Use batch API if available
        return []
    
    def select_model(self, task: str) -> str:
        """
        Select appropriate model based on task.
        
        Args:
            task: Task description
            
        Returns:
            Model name
        """
        # TODO: Implement model selection logic
        # TODO: Return appropriate model
        return "gpt-4o-mini"
    
    def get_cost_dashboard(self) -> Dict:
        """Get cost dashboard data."""
        # TODO: Aggregate cost data
        # TODO: Calculate metrics
        return {
            "total_cost": 0.0,
            "by_model": {},
            "by_task": {}
        }


def main():
    """Main function."""
    print("💰 Cost-Optimized AI System")
    print("Type 'quit' to exit\n")
    
    # TODO: Initialize optimizer
    # optimizer = CostOptimizer()
    
    # TODO: Implement main loop


if __name__ == "__main__":
    main()
