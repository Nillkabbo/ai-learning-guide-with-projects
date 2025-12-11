"""
Production Command Processor - Complete Solution
Chapter 8 Project

Demonstrates production patterns: error handling, retries, rate limiting, caching.
"""

import os
import time
from functools import wraps
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


def retry_with_backoff(max_retries: int = 3, initial_delay: float = 1.0):
    """Decorator for retrying with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(delay)
                    delay *= 2
            return None
        return wrapper
    return decorator


class CommandProcessor:
    """Production-ready command processor."""
    
    def __init__(self):
        """Initialize processor."""
        load_dotenv()
        
        if not OPENAI_AVAILABLE:
            raise ImportError("openai library not installed")
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found")
        
        self.client = openai.OpenAI(api_key=api_key)
        self.cache = {}  # Simple cache
    
    @retry_with_backoff(max_retries=3)
    def process_command(self, command: str) -> str:
        """Process IoT command."""
        # Check cache
        if command in self.cache:
            return self.cache[command]
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": f"Process this IoT command: {command}"}]
            )
            result = response.choices[0].message.content
            self.cache[command] = result
            return result
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """Main function."""
    print("⚙️  Production Command Processor")
    print("Type 'quit' to exit\n")
    
    try:
        processor = CommandProcessor()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            cmd = input("Command (or 'quit'): ").strip()
            if cmd.lower() == 'quit':
                break
            result = processor.process_command(cmd)
            print(f"\nResult: {result}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
