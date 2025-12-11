# Chapter 8: API Design Patterns and Best Practices

Building a simple AI application is one thing; building a robust, scalable, and resilient one is an entirely different engineering challenge. As you move from prototypes to production, your application will face the harsh realities of the real world: network failures, API rate limits, service outages, and unpredictable user load.

This chapter is your guide to building production-grade AI systems. We will explore a set of battle-tested design patterns that address the unique challenges of working with third-party AI APIs. These patterns are not just about making your code work; they are about making it work reliably, efficiently, and cost-effectively under pressure. By mastering these techniques, you will be able to build applications that are not only intelligent but also enterprise-ready.

### Learning Objectives

By the end of this chapter, you will be able to:

-   Implement robust retry strategies with exponential backoff to handle transient API failures.
-   Design and build rate limiters that respect different AI provider quotas.
-   Choose and implement the correct response pattern—streaming or batching—for different use cases.
-   Create efficient, multi-level caching strategies to reduce latency and API costs.
-   Design a multi-provider architecture with load balancing and automatic failover for high availability.
-   Build a complete, production-ready IoT command processing system that incorporates these patterns.

## The Foundation: Robust Error Handling

Before we explore advanced patterns, we must master the basics. A production application never crashes because of a failed API call; it anticipates failure and handles it gracefully.

### From Naive to Nuanced Error Handling

A simple `try...except` block is the first step, but it's not enough.

```python
# A naive approach: catches everything, but tells you nothing.
def naive_ai_call(prompt: str):
    try:
        # ... API call ...
    except Exception as e:
        print(f"Something went wrong: {e}")
        return None
```

A much better approach is to catch *specific* error types that the API library provides. This allows you to react differently to different kinds of failures. For example, a `RateLimitError` is temporary and can be retried, while an `AuthenticationError` is permanent and should not be.

#### Using OpenAI

```python
import openai
from typing import Optional

def better_error_handling(prompt: str) -> Optional[str]:
    """Handles specific, known exceptions from the OpenAI library."""
    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except openai.RateLimitError as e:
        print(f"Rate limit exceeded. Please wait before trying again. Details: {e}")
        return None
    except openai.AuthenticationError as e:
        print(f"Authentication failed. Check your API key. Details: {e}")
        return None
    except openai.APIError as e:
        print(f"An OpenAI API error occurred: {e}")
        return None
```

#### Using Ollama

```python
import ollama
from typing import Optional

def better_error_handling(prompt: str, model: str = "llama2") -> Optional[str]:
    """Handles specific, known exceptions from the Ollama library."""
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        # Ollama doesn't have specific exception types like OpenAI
        # Check error message content to determine error type
        error_msg = str(e).lower()
        if "connection" in error_msg or "refused" in error_msg:
            print(f"Connection failed. Is Ollama running? Details: {e}")
            return None
        elif "model" in error_msg and "not found" in error_msg:
            print(f"Model not found. Install with: ollama pull {model}. Details: {e}")
            return None
        else:
            print(f"An Ollama API error occurred: {e}")
            return None
```

**Note**: Ollama uses generic Python exceptions rather than custom exception types. Error handling relies on checking error message content or HTTP status codes if using Ollama's HTTP API directly.

## Pattern 1: Retries with Exponential Backoff

Network glitches and temporary service overloads are common. A simple retry can often resolve the issue. However, retrying immediately can make the problem worse, contributing to a "thundering herd" that overwhelms the service.

The professional solution is **exponential backoff with jitter**.
-   **Exponential Backoff:** The delay between retries increases exponentially (e.g., 1s, 2s, 4s, 8s).
-   **Jitter:** A small, random amount of time is added to the delay to prevent multiple clients from retrying at the exact same moment.

While you can implement this manually, the `tenacity` library provides a clean, declarative way to add robust retry logic to any function.

First, install `tenacity`:
```bash
pip install tenacity
```

Now, we can add a simple decorator to our function to make it resilient.

#### Using OpenAI

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import openai

@retry(
    # Stop retrying after 3 attempts.
    stop=stop_after_attempt(3),
    # Wait 1s, then 2s, then 4s, etc., with a max wait of 10s.
    wait=wait_exponential(multiplier=1, min=1, max=10),
    # Only retry on specific, transient errors like RateLimitError.
    retry=retry_if_exception_type((openai.RateLimitError, openai.APITimeoutError))
)
def robust_ai_call(prompt: str) -> str:
    """A production-ready AI call with automatic retries."""
    print("Attempting to call OpenAI API...")
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

#### Using Ollama

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import ollama

def is_transient_error(exception: Exception) -> bool:
    """Check if an error is transient and should be retried."""
    error_msg = str(exception).lower()
    # Retry on connection errors, but not on model-not-found errors
    return "connection" in error_msg or "refused" in error_msg or "timeout" in error_msg

@retry(
    # Stop retrying after 3 attempts.
    stop=stop_after_attempt(3),
    # Wait 1s, then 2s, then 4s, etc., with a max wait of 10s.
    wait=wait_exponential(multiplier=1, min=1, max=10),
    # Retry on transient errors (connection issues)
    retry=retry_if_exception_type(Exception) if is_transient_error else None
)
def robust_ai_call(prompt: str, model: str = "llama2") -> str:
    """A production-ready AI call with automatic retries."""
    print(f"Attempting to call Ollama API (model: {model})...")
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
```

**Note**: For Ollama, retry logic focuses on connection errors since local models typically don't have rate limits. However, you may want to retry if Ollama's service is temporarily unavailable.

# You can call this function normally; tenacity handles the retries behind the scenes.
try:
    result = robust_ai_call("Write a short poem about resilient code.")
    print(result)
except Exception as e:
    print(f"The API call failed even after several retries: {e}")
```
This decorator transforms a simple function into a resilient one that can automatically recover from temporary network and API issues.

## Pattern 2: Intelligent Rate Limiting

Every AI provider imposes rate limits—a maximum number of requests or tokens you can send per minute. Exceeding these limits will result in `RateLimitError` exceptions. A well-behaved application anticipates and respects these limits *before* making a call.

A common way to do this is with the **token bucket algorithm**. Imagine each user has a bucket that can hold a certain number of "request tokens." The bucket is refilled at a constant rate. To make a request, you must take a token from the bucket. If the bucket is empty, you must wait.

```python
import time

class TokenBucketRateLimiter:
    def __init__(self, requests_per_minute: int):
        self.capacity = requests_per_minute
        self.tokens_per_second = requests_per_minute / 60.0
        self.tokens = float(self.capacity)
        self.last_update_time = time.monotonic()

    def can_proceed(self) -> bool:
        """Checks if a request can be made, consuming a token if so."""
        now = time.monotonic()
        
        # Add new tokens that have accrued since the last update
        elapsed_time = now - self.last_update_time
        self.tokens += elapsed_time * self.tokens_per_second
        self.tokens = min(self.capacity, self.tokens) # Cap at max capacity
        
        self.last_update_time = now
        
        # Check if there are enough tokens to proceed
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False

# Example: Simulate calls for a user on a free tier (e.g., 20 RPM)
limiter = TokenBucketRateLimiter(requests_per_minute=20)

for i in range(25):
    if limiter.can_proceed():
        print(f"Request #{i+1}: Allowed")
    else:
        print(f"Request #{i+1}: Denied. Must wait.")
    time.sleep(0.1) # Simulate rapid requests
```
By checking `limiter.can_proceed()` before each API call, your application can intelligently throttle itself to avoid hitting API rate limits.

## Pattern 3: Adaptive Response Handling (Streaming vs. Batching)

Not all user requests are the same. A request for a quick fact needs a fast, complete response. A request to "write a detailed report" is better suited for a streaming response that shows progress immediately. A well-designed system can adapt its response strategy.

-   **Batch Response:** The default. Wait for the full AI response, then send it to the client. Best for short, predictable queries.
-   **Streaming Response:** Send the response to the client token-by-token. Best for long-form content generation to improve perceived performance.

Here's an adaptive function that decides which strategy to use.

#### Using OpenAI

```python
from typing import Union, Iterator
import openai

def adaptive_ai_response(prompt: str) -> Union[str, Iterator[str]]:
    """Automatically chooses to stream or not based on the prompt."""
    
    # Heuristic: If the prompt asks for long-form content, enable streaming.
    streaming_keywords = ['write', 'explain', 'describe', 'story', 'report', 'detailed']
    should_stream = any(keyword in prompt.lower() for keyword in streaming_keywords)
    
    client = openai.OpenAI()
    
    if should_stream:
        print("-> Using streaming response.")
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        # Return the generator object for the client to iterate over
        return (chunk.choices[0].delta.content or "" for chunk in stream)
    else:
        print("-> Using batch response.")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

# Test with a short query
result = adaptive_ai_response("What is the capital of Japan?")
print(result)

# Test with a long query
stream_result = adaptive_ai_response("Write a short story about a brave knight.")
for chunk in stream_result:
    print(chunk, end="", flush=True)
print()
```

#### Using Ollama

```python
from typing import Union, Iterator
import ollama

def adaptive_ai_response(prompt: str, model: str = "llama2") -> Union[str, Iterator[str]]:
    """Automatically chooses to stream or not based on the prompt."""
    
    # Heuristic: If the prompt asks for long-form content, enable streaming.
    streaming_keywords = ['write', 'explain', 'describe', 'story', 'report', 'detailed']
    should_stream = any(keyword in prompt.lower() for keyword in streaming_keywords)
    
    if should_stream:
        print("-> Using streaming response.")
        stream = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        # Return the generator object for the client to iterate over
        return (chunk.get("message", {}).get("content", "") for chunk in stream)
    else:
        print("-> Using batch response.")
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']

# Test with a short query
result = adaptive_ai_response("What is the capital of Japan?")
print(result)

# Test with a long query
stream_result = adaptive_ai_response("Write a short story about a brave knight.")
for chunk in stream_result:
    print(chunk, end="", flush=True)
print()
```

## Pattern 4: Intelligent Caching

API calls are the most expensive and time-consuming part of any AI application. An effective caching strategy is crucial for both performance and cost management. For production, a distributed cache like **Redis** is essential, as it allows multiple instances of your application to share the same cache.

### Production-Ready Caching with Redis

First, install the Redis Python client: `pip install redis`.

```python
import redis
import json
import hashlib

class RedisAICache:
    def __init__(self, redis_url: str = "redis://localhost:6379", default_ttl: int = 3600):
        self.redis_client = redis.from_url(redis_url, decode_responses=True)
        self.default_ttl = default_ttl # Default cache time: 1 hour

    def _create_key(self, model: str, prompt: str) -> str:
        """Creates a unique and consistent key for a given request."""
        # Use a hash to create a short, fixed-length key
        payload = {"model": model, "prompt": prompt}
        return f"ai_cache:{hashlib.md5(json.dumps(payload).encode()).hexdigest()}"

    def get(self, model: str, prompt: str) -> Optional[str]:
        key = self._create_key(model, prompt)
        return self.redis_client.get(key)

    def set(self, model: str, prompt: str, response: str):
        key = self._create_key(model, prompt)
        self.redis_client.setex(key, self.default_ttl, response)

# --- Integrating the cache into our AI call function ---
cache = RedisAICache()

def cached_robust_ai_call(prompt: str) -> str:
    """A robust AI call that first checks a Redis cache."""
    model = "gpt-4o-mini"
    
    # 1. Check the cache first
    cached_response = cache.get(model, prompt)
    if cached_response:
        print("-> Cache Hit!")
        return cached_response
        
    print("-> Cache Miss. Calling API...")
    # 2. If not in cache, make the API call
    response = robust_ai_call(prompt) # Using our retry function from earlier
    
    # 3. Store the new response in the cache
    cache.set(model, prompt, response)
    
    return response

# The first call will be slow and hit the API.
print(cached_robust_ai_call("What is Zigbee?"))
# The second call will be instantaneous.
print(cached_robust_ai_call("What is Zigbee?"))
```

## Pattern 5: Multi-Provider Failover and Load Balancing

Relying on a single AI provider is risky. Services can experience outages or performance degradation. A resilient architecture uses multiple providers and can automatically switch between them.

### An Abstraction Layer for AI Providers

First, we create a common interface for different providers.

#### Using OpenAI, Anthropic, and Google

```python
from enum import Enum
import openai
import anthropic
import google.generativeai as genai

class AIProviderEnum(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"

class MultiProviderClient:
    def __init__(self):
        # Initialize clients for each provider
        self.clients = {
            AIProviderEnum.OPENAI: openai.OpenAI(),
            AIProviderEnum.ANTHROPIC: anthropic.Anthropic(),
            AIProviderEnum.GOOGLE: genai.GenerativeModel('gemini-1.5-flash')
        }
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # Special config for Google

    def call(self, provider: AIProviderEnum, prompt: str) -> str:
        """Makes a call using the specified provider's API syntax."""
        print(f"--> Calling {provider.value}...")
        client = self.clients[provider]
        
        if provider == AIProviderEnum.OPENAI:
            # ... OpenAI call syntax ...
            return "OpenAI Response"
        elif provider == AIProviderEnum.ANTHROPIC:
            # ... Anthropic call syntax ...
            return "Anthropic Response"
        elif provider == AIProviderEnum.GOOGLE:
            # ... Google call syntax ...
            return "Google Response"
        raise ValueError("Unknown provider")

```

### A Simple Failover Router

Now, we can build a router that tries providers in a preferred order until one succeeds.

```python
class FailoverRouter:
    def __init__(self, client: MultiProviderClient):
        self.client = client
        # Define the preferred order of providers
        self.provider_preference = [
            AIProviderEnum.OPENAI, 
            AIProviderEnum.ANTHROPIC, 
            AIProviderEnum.GOOGLE
        ]

    def call_with_failover(self, prompt: str) -> str:
        """Tries each provider in order until one succeeds."""
        for provider in self.provider_preference:
            try:
                response = self.client.call(provider, prompt)
                if response:
                    print(f"Success with {provider.value}!")
                    return response
            except Exception as e:
                print(f"Provider {provider.value} failed: {e}. Trying next...")
        
        return "Error: All AI providers are currently unavailable."

# --- Usage ---
multi_client = MultiProviderClient()
router = FailoverRouter(multi_client)
result = router.call_with_failover("Explain the concept of an API.")
print(f"Final Result: {result}")
```

This simple failover logic dramatically increases the uptime and reliability of your application. More advanced routers could incorporate health checks and performance metrics to choose the best provider dynamically.

**Note**: Ollama can be added as a provider option in the multi-provider architecture. Since Ollama runs locally, it can serve as a reliable fallback when cloud providers are unavailable, or as the primary provider for cost-sensitive applications. The failover pattern works identically—simply add `AIProviderEnum.OLLAMA` to the provider list and implement the Ollama call logic in the `call` method.

## Conclusion: Building for the Real World

You have now learned five essential patterns for building production-ready AI applications. These techniques—retries, rate limiting, adaptive responses, caching, and failover—are the building blocks of robust and scalable systems.

-   **Start with robust error handling.**
-   **Wrap your calls in a retry decorator** (`tenacity` is your friend).
-   **Implement a rate limiter** to avoid hitting API quotas.
-   **Use adaptive streaming** for a better user experience.
-   **Cache aggressively with Redis** to improve speed and save money.
-   **Build a multi-provider failover system** for maximum reliability.

By incorporating these patterns into your development workflow, you move from being a user of AI APIs to being an architect of intelligent systems. You are now prepared to build applications that can withstand the rigors of a production environment.

# References and Further Reading

- 5 Essential API Design Patterns for Successful AI Model Implementation. https://dev.to/stellaacharoiro/5-essential-api-design-patterns-for-successful-ai-model-implementation-2dkk
- Beyond the Gang of Four: Practical Design Patterns for Modern AI Systems. https://www.infoq.com/articles/practical-design-patterns-modern-ai-systems/
- Generative AI Design Patterns: A Comprehensive Guide. https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0
- AI Patterns: A Structured Approach to Artificial Intelligence Development. https://medium.com/@xavier.mehaut/ai-patterns-a-structured-approach-to-artificial-intelligence-development-9d97903c8e34