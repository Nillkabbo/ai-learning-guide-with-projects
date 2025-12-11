"""
Cost-Optimized AI System - Complete Solution
Chapter 21 Project

Demonstrates cost optimization: caching, batch processing, model selection, cost tracking.
"""

import os
from typing import Dict, List
from collections import defaultdict
from dotenv import load_dotenv
from cachetools import TTLCache
import tiktoken

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Model pricing (per 1M tokens)
PRICING = {
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50}
}


class CostOptimizer:
    """Cost-optimized AI system."""
    
    def __init__(self):
        """Initialize cost optimizer."""
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or not OPENAI_AVAILABLE:
            raise ValueError("OpenAI API key required")
        
        self.client = openai.OpenAI(api_key=api_key)
        self.cache = TTLCache(maxsize=1000, ttl=3600)  # 1 hour TTL
        self.encoder = tiktoken.encoding_for_model("gpt-4o-mini")
        self.cost_tracker = defaultdict(float)
        self.usage_stats = defaultdict(int)
    
    def track_cost(self, tokens: int, model: str, is_input: bool = True) -> float:
        """Track and calculate cost."""
        pricing = PRICING.get(model, PRICING["gpt-4o-mini"])
        rate = pricing["input"] if is_input else pricing["output"]
        cost = (tokens / 1_000_000) * rate
        
        self.cost_tracker[model] += cost
        self.usage_stats[model] += tokens
        
        return cost
    
    def get_cached_response(self, prompt: str) -> str:
        """Get cached response if available."""
        cache_key = hash(prompt)
        if cache_key in self.cache:
            return self.cache[cache_key]
        return None
    
    def process_with_cache(self, prompt: str, model: str = "gpt-4o-mini") -> str:
        """Process prompt with caching."""
        # Check cache
        cached = self.get_cached_response(prompt)
        if cached:
            return cached
        
        # Make API call
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            
            # Track cost
            if response.usage:
                self.track_cost(response.usage.prompt_tokens, model, True)
                self.track_cost(response.usage.completion_tokens, model, False)
            
            # Cache result
            cache_key = hash(prompt)
            self.cache[cache_key] = result
            
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def batch_process(self, prompts: List[str], model: str = "gpt-4o-mini") -> List[str]:
        """Process multiple prompts efficiently."""
        results = []
        for prompt in prompts:
            # Check cache first
            cached = self.get_cached_response(prompt)
            if cached:
                results.append(cached)
            else:
                result = self.process_with_cache(prompt, model)
                results.append(result)
        return results
    
    def select_model(self, task: str) -> str:
        """Select appropriate model based on task complexity."""
        # Simple heuristic: use cheaper model for simple tasks
        simple_keywords = ["explain", "summarize", "translate"]
        if any(kw in task.lower() for kw in simple_keywords):
            return "gpt-4o-mini"
        return "gpt-4o-mini"  # Default to cheapest
    
    def get_cost_dashboard(self) -> Dict:
        """Get cost dashboard data."""
        total_cost = sum(self.cost_tracker.values())
        total_tokens = sum(self.usage_stats.values())
        
        return {
            "total_cost": total_cost,
            "total_tokens": total_tokens,
            "by_model": dict(self.cost_tracker),
            "cache_hits": len(self.cache),
            "cache_size": len(self.cache)
        }


def main():
    """Main function."""
    print("💰 Cost-Optimized AI System")
    print("Type 'quit' to exit\n")
    
    try:
        optimizer = CostOptimizer()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            prompt = input("Prompt (or 'quit'): ").strip()
            if prompt.lower() == 'quit':
                break
            
            if not prompt:
                continue
            
            # Select model
            model = optimizer.select_model(prompt)
            print(f"Using model: {model}")
            
            # Process with caching
            response = optimizer.process_with_cache(prompt, model)
            print(f"\nResponse: {response}\n")
            
            # Show dashboard
            dashboard = optimizer.get_cost_dashboard()
            print(f"Total cost: ${dashboard['total_cost']:.6f}")
            print(f"Cache hits: {dashboard['cache_hits']}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")
    
    # Final dashboard
    dashboard = optimizer.get_cost_dashboard()
    print(f"\nFinal Cost Summary:")
    print(f"Total: ${dashboard['total_cost']:.6f}")
    print(f"Tokens: {dashboard['total_tokens']:,}")


if __name__ == "__main__":
    main()
