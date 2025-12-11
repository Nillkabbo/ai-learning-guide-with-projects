# Chapter 5: A Developer's Guide to the OpenAI API

In the previous chapters, we explored the concepts behind AI. Now, it's time to roll up our sleeves and become practitioners. This chapter is a complete, hands-on guide to the OpenAI API, the tool that allows your Python applications to communicate with powerful models like GPT-4. We will move from the simplest possible API call to building sophisticated applications that use function calling, vision, and audio.

By the end of this chapter, you will not just understand the API; you will be proficient in using it to build real-world, intelligent applications.

### Learning Objectives

By the end of this chapter, you will be able to:

-   Make your first successful OpenAI API call from Python.
-   Structure conversations with system messages to give your AI a distinct personality.
-   Manage conversation history to provide your AI with memory.
-   Control AI creativity and response length using `temperature` and `max_tokens`.
-   Implement streaming for real-time, interactive user experiences.
-   Give your AI tools by implementing **function calling**.
-   Analyze images and process audio using multimodal models.
-   Build a practical e-commerce recommendation assistant from scratch.

## Your First API Call: The "Hello, World!" of AI

Every programming journey begins with a "Hello, World!" example. For the OpenAI API, it's a simple request that asks the model to say hello. This small step contains the core pattern of every interaction you will ever have with the API.

### The Absolute Minimum Code

Here are the essential lines required to talk to an AI model.

#### Using OpenAI

```python
import openai

# 1. Initialize the client. It automatically looks for the
#    OPENAI_API_KEY environment variable.
client = openai.OpenAI()

# 2. Create a request to the chat completions endpoint.
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Say hello to the AI world!"}
    ]
)

# 3. Extract the text from the response object.
ai_message = response.choices[0].message.content
print(ai_message)
```

#### Using Ollama (Local)

```python
import ollama

# 1. Ollama runs locally, no API key needed
#    Make sure Ollama is running: ollama serve

# 2. Create a request to the local Ollama instance
response = ollama.chat(
    model="llama2",  # or mistral, codellama, etc.
    messages=[
        {"role": "user", "content": "Say hello to the AI world!"}
    ]
)

# 3. Extract the text from the response (Ollama uses dictionary structure)
ai_message = response["message"]["content"]
print(ai_message)
```

That's it. You've sent a message to a state-of-the-art AI and received a response. Both OpenAI (cloud) and Ollama (local) use the same message structure, making it easy to switch between them. Let's formalize this into a reusable function, incorporating the secure API key handling we learned in Chapter 3.

### A Practical, Reusable Function

#### Using OpenAI

```python
import openai
import os
from dotenv import load_dotenv

# Load your API key from a .env file for security
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(prompt: str) -> str:
    """Sends a single prompt to the AI and returns the response."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Let's test it
explanation = ask_ai("Explain what an API is in one simple sentence.")
print(f"AI Response: {explanation}")
```

#### Using Ollama

```python
import ollama

def ask_ai(prompt: str, model: str = "llama2") -> str:
    """Sends a single prompt to the local Ollama model and returns the response."""
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"An error occurred: {e}. Make sure Ollama is running and the model is pulled."

# Let's test it
explanation = ask_ai("Explain what an API is in one simple sentence.")
print(f"AI Response: {explanation}")
```

## System Messages: Giving Your AI a Personality

By default, the AI acts as a generic "helpful assistant." To build specialized applications, you need to give it a role, a personality, and a set of instructions. This is done with the **system message**. It's the first message in the conversation and acts as a high-level directive for the AI's behavior.

Let's see the difference. Without a system message, the AI is noncommittal.

```python
# A generic response without a system message
question = "What should I wear for a business meeting?"
print(f"Generic Assistant: {ask_ai(question)}")
```

Now, let's add a system message to turn our AI into a fashion expert.

#### Using OpenAI

```python
def ask_fashion_expert(prompt: str) -> str:
    """Asks a question to an AI configured as a fashion expert."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a world-class fashion consultant. You give confident, stylish, and modern advice."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print(f"Fashion Expert: {ask_fashion_expert(question)}")
```

#### Using Ollama

```python
import ollama

def ask_fashion_expert(prompt: str, model: str = "llama2") -> str:
    """Asks a question to an AI configured as a fashion expert."""
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "You are a world-class fashion consultant. You give confident, stylish, and modern advice."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]

print(f"Fashion Expert: {ask_fashion_expert(question)}")
```

The system message completely changes the tone, style, and content of the response. This is your primary tool for tailoring the AI to your specific application. Both OpenAI and Ollama support system messages identically.

## Building Conversations: Giving Your AI Memory

An AI's "memory" is simply the history of the conversation that you provide with each new request. A single API call is stateless; it has no memory of past interactions. To create a conversation, you must manage the history yourself and send it with every new message.

Let's build a simple chatbot class that handles this automatically.

#### Using OpenAI

```python
class SimpleChatbot:
    def __init__(self, system_prompt: str = "You are a helpful assistant."):
        # The conversation history starts with the system prompt.
        self.conversation_history = [
            {"role": "system", "content": system_prompt}
        ]
    
    def chat(self, user_message: str) -> str:
        """Adds a user message to the history and gets the AI's response."""
        
        # Add the user's new message to the history
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # Send the entire history to the AI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.conversation_history
        )
        
        ai_message = response.choices[0].message.content
        
        # Add the AI's response to the history for the next turn
        self.conversation_history.append({"role": "assistant", "content": ai_message})
        
        return ai_message

# Let's test the chatbot's memory
iot_expert_bot = SimpleChatbot("You are a friendly IoT expert.")

print("Bot:", iot_expert_bot.chat("My temperature sensor is giving weird readings."))
print("Bot:", iot_expert_bot.chat("They are all exactly 25.0°C, which seems unlikely."))
print("Bot:", iot_expert_bot.chat("What could cause that?"))
```

#### Using Ollama

```python
import ollama

class SimpleChatbot:
    def __init__(self, system_prompt: str = "You are a helpful assistant.", model: str = "llama2"):
        # The conversation history starts with the system prompt.
        self.conversation_history = [
            {"role": "system", "content": system_prompt}
        ]
        self.model = model
    
    def chat(self, user_message: str) -> str:
        """Adds a user message to the history and gets the AI's response."""
        
        # Add the user's new message to the history
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # Send the entire history to the AI
        response = ollama.chat(
            model=self.model,
            messages=self.conversation_history
        )
        
        ai_message = response["message"]["content"]
        
        # Add the AI's response to the history for the next turn
        self.conversation_history.append({"role": "assistant", "content": ai_message})
        
        return ai_message

# Let's test the chatbot's memory
iot_expert_bot = SimpleChatbot("You are a friendly IoT expert.", model="llama2")

print("Bot:", iot_expert_bot.chat("My temperature sensor is giving weird readings."))
print("Bot:", iot_expert_bot.chat("They are all exactly 25.0°C, which seems unlikely."))
print("Bot:", iot_expert_bot.chat("What could cause that?"))
```

Because we send the full history each time, the AI's final response is context-aware. It knows we're talking about a temperature sensor reading exactly 25.0°C and can provide a relevant diagnosis. Both OpenAI and Ollama handle conversation history identically.

## Controlling Creativity: Temperature and Max Tokens

The API gives you several "dials" to control the AI's output. The most important one is `temperature`.

-   **Temperature:** Controls the randomness of the output.
    -   `0.0`: Very deterministic and focused. Good for factual queries and code generation.
    -   `~0.7`: A good balance of creativity and coherence.
    -   `1.0` or higher: Very creative and potentially less coherent. Good for brainstorming.

#### Using OpenAI

```python
def test_temperature(prompt: str, temp: float) -> str:
    """Tests the effect of different temperature settings."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=temp
    )
    return response.choices[0].message.content

prompt = "Write a one-sentence tagline for a smart coffee mug."

print(f"Temp 0.0: {test_temperature(prompt, 0.0)}")
print(f"Temp 0.0: {test_temperature(prompt, 0.0)}") # Will likely be the same
print(f"Temp 1.0: {test_temperature(prompt, 1.0)}")
print(f"Temp 1.0: {test_temperature(prompt, 1.0)}") # Will likely be different
```

#### Using Ollama

```python
import ollama

def test_temperature(prompt: str, temp: float, model: str = "llama2") -> str:
    """Tests the effect of different temperature settings."""
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": temp,
            # Ollama also supports num_predict (equivalent to max_tokens)
            # "num_predict": 100
        }
    )
    return response["message"]["content"]

prompt = "Write a one-sentence tagline for a smart coffee mug."

print(f"Temp 0.0: {test_temperature(prompt, 0.0)}")
print(f"Temp 0.0: {test_temperature(prompt, 0.0)}") # Will likely be the same
print(f"Temp 1.0: {test_temperature(prompt, 1.0)}")
print(f"Temp 1.0: {test_temperature(prompt, 1.0)}") # Will likely be different
```

-   **`max_tokens` (OpenAI) / `num_predict` (Ollama)**: Sets a hard limit on the length of the AI's response. This is useful for controlling costs (OpenAI) or response length (Ollama).

**Note**: Ollama uses `options` dictionary for parameters like `temperature` and `num_predict`, while OpenAI uses direct parameters. Both achieve the same effect.

## Streaming Responses: Real-Time Interaction

For a better user experience, especially with longer responses, you can **stream** the output. This sends the response back to your application token-by-token as it's generated, allowing you to display it in real time, just like ChatGPT's "typing" effect.

#### Using OpenAI

```python
def stream_a_story():
    """Demonstrates a streaming API call."""
    prompt = "Tell me a short story about a robot who learns to paint."
    
    # Setting stream=True returns an iterable stream object
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    
    print("AI Story: ", end="")
    for chunk in stream:
        # Each 'chunk' contains a small piece of the response
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print() # For a final newline

stream_a_story()
```

#### Using Ollama

```python
import ollama

def stream_a_story():
    """Demonstrates a streaming API call with Ollama."""
    prompt = "Tell me a short story about a robot who learns to paint."
    
    # Ollama streams by default, returns a generator
    stream = ollama.chat(
        model="llama2",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    
    print("AI Story: ", end="")
    for chunk in stream:
        # Each 'chunk' is a dictionary with the message content
        if "message" in chunk and "content" in chunk["message"]:
            content = chunk["message"]["content"]
            if content:
                print(content, end="", flush=True)
    print() # For a final newline

stream_a_story()
```

Both OpenAI and Ollama support streaming, providing a smooth real-time user experience. Ollama's streaming is particularly useful for local models as it provides immediate feedback.

## Function Calling: Giving Your AI Superpowers

This is one ofthe most powerful features of the OpenAI API. **Function calling** allows you to describe your own Python functions to the AI, and the AI can then choose to "call" them to get information or perform actions.

This is how you connect your AI to the outside world—to databases, other APIs, or hardware.

The process has two steps:
1.  **AI decides to call a function:** You send a prompt and a list of available "tools" (your functions). The AI responds not with text, but with a JSON object saying, "I want to call the `get_weather` function with the `location` argument set to 'Tokyo'."
2.  **You execute the function:** Your code receives this, runs your actual `get_weather('Tokyo')` Python function, and then sends the result back to the AI in a second API call. The AI then uses this new information to generate its final, user-facing response.

### A Simple Weather Bot Example

#### Using OpenAI

```python
import json

# This is our actual tool. It could be any Python function.
def get_current_weather(location: str):
    """A dummy function to get weather data."""
    print(f"--- Calling weather tool for {location} ---")
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "15°C", "condition": "Cloudy"})
    elif "london" in location.lower():
        return json.dumps({"location": "London", "temperature": "10°C", "condition": "Rainy"})
    return json.dumps({"error": "Location not found"})

def weather_bot(user_prompt: str):
    messages = [{"role": "user", "content": user_prompt}]
    
    # The 'tools' parameter describes our function to the AI.
    tools = [{
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location.",
            "parameters": {
                "type": "object",
                "properties": {"location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}},
                "required": ["location"],
            },
        },
    }]

    # Step 1: First call to see if the AI wants to use a tool
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message
    
    # Check if the AI returned a tool call
    if not response_message.tool_calls:
        return response_message.content

    # Step 2: AI wants to use a tool. Execute it.
    tool_call = response_message.tool_calls[0]
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)
    
    # Call our actual Python function
    function_response = get_current_weather(location=function_args.get("location"))

    # Step 3: Send the tool's result back to the AI
    messages.append(response_message) # Add AI's previous turn
    messages.append({ # Add the function result
        "tool_call_id": tool_call.id,
        "role": "tool",
        "name": function_name,
        "content": function_response,
    })
    
    final_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    return final_response.choices[0].message.content

print(weather_bot("What's the weather in Tokyo?"))
print(weather_bot("Should I bring an umbrella if I'm going to London today?"))
```

#### Using Ollama (Function Calling Support)

**Note**: Function calling support in Ollama varies by model. Some models like `llama3.2` and newer versions support structured outputs and function calling. For models without native function calling, you can use prompt engineering to achieve similar results.

```python
import json
import ollama

# This is our actual tool. It could be any Python function.
def get_current_weather(location: str):
    """A dummy function to get weather data."""
    print(f"--- Calling weather tool for {location} ---")
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "15°C", "condition": "Cloudy"})
    elif "london" in location.lower():
        return json.dumps({"location": "London", "temperature": "10°C", "condition": "Rainy"})
    return json.dumps({"error": "Location not found"})

def weather_bot(user_prompt: str, model: str = "llama3.2"):
    """
    Weather bot using Ollama.
    Note: Function calling support depends on the model.
    For models without function calling, we use prompt engineering.
    """
    # Describe the available function in the system message
    system_message = """You are a helpful weather assistant. When asked about weather, 
    you should call the get_current_weather function. Respond with JSON in this format:
    {"function": "get_current_weather", "arguments": {"location": "city name"}}
    If no function call is needed, respond normally."""
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt}
    ]
    
    # Step 1: Ask the AI if it needs to call a function
    response = ollama.chat(
        model=model,
        messages=messages,
        options={"temperature": 0.1}  # Lower temperature for more structured output
    )
    
    ai_response = response["message"]["content"]
    
    # Step 2: Check if the response contains a function call
    try:
        # Try to parse JSON function call
        if "function" in ai_response.lower() or "{" in ai_response:
            # Extract JSON from response
            import re
            json_match = re.search(r'\{[^}]+\}', ai_response)
            if json_match:
                function_call = json.loads(json_match.group())
                if function_call.get("function") == "get_current_weather":
                    location = function_call.get("arguments", {}).get("location", "")
                    function_response = get_current_weather(location)
                    
                    # Step 3: Send function result back to AI
                    messages.append({"role": "assistant", "content": ai_response})
                    messages.append({
                        "role": "user",
                        "content": f"Function result: {function_response}. Now provide a natural language response."
                    })
                    
                    final_response = ollama.chat(
                        model=model,
                        messages=messages
                    )
                    return final_response["message"]["content"]
    except:
        pass
    
    # If no function call detected, return the original response
    return ai_response

print(weather_bot("What's the weather in Tokyo?"))
print(weather_bot("Should I bring an umbrella if I'm going to London today?"))
```

**Important Note**: Ollama's function calling support is model-dependent. Newer models like `llama3.2`, `mistral`, and `qwen2.5` have better structured output support. For production use, consider using OpenAI's function calling or implementing a more robust prompt-based approach with Ollama.

## Multimodal Capabilities: Vision and Audio

The latest models are multimodal, meaning they can process more than just text.

### Vision: Analyzing Images

#### Using OpenAI

You can provide an image URL or a base64-encoded local image and ask the AI questions about it.

```python
def analyze_image(image_url: str, prompt: str):
    """Asks the AI a question about an image."""
    response = client.chat.completions.create(
        model="gpt-4o", # Use a vision-capable model
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": image_url}},
            ],
        }],
        max_tokens=300,
    )
    return response.choices[0].message.content

# A public domain image of a cat
cat_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat_paw.jpg/1280px-Cat_paw.jpg"
print(analyze_image(cat_image_url, "Describe this image in detail."))
```

#### Using Ollama (Vision Support)

**Note**: Vision support in Ollama requires vision-capable models like `llava`, `bakllava`, or `llava-llama3`. These models can process images but require base64 encoding of local images.

```python
import ollama
import base64
from pathlib import Path

def analyze_image(image_path: str, prompt: str, model: str = "llava"):
    """
    Analyzes an image using Ollama's vision-capable models.
    
    Args:
        image_path: Path to local image file
        prompt: Question about the image
        model: Vision-capable model (llava, bakllava, etc.)
    """
    # Read and encode the image
    image_bytes = Path(image_path).read_bytes()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    
    # Ollama vision models accept images in the messages
    response = ollama.chat(
        model=model,
        messages=[{
            "role": "user",
            "content": prompt,
            "images": [image_base64]  # Ollama uses 'images' array with base64
        }],
        options={"num_predict": 300}
    )
    return response["message"]["content"]

# Example usage with a local image
# First pull a vision model: ollama pull llava
# print(analyze_image("path/to/image.jpg", "Describe this image in detail."))
```

**Important**: Ollama vision models require:
1. Pulling a vision-capable model: `ollama pull llava`
2. Local image files (base64 encoded), not URLs
3. More RAM than text-only models (typically 8GB+)

### Audio: Speech-to-Text and Text-to-Speech

#### Using OpenAI

The API also provides powerful audio models.

-   **Whisper** for speech-to-text transcription.
-   **TTS (Text-to-Speech)** for generating human-like audio from text.

```python
def text_to_speech_demo():
    """Converts text into an audio file."""
    text = "Hello from the OpenAI Text-to-Speech API! I can create natural-sounding audio."
    
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy", # Other voices: echo, fable, onyx, nova, shimmer
        input=text
    )
    
    # The response content is the raw audio data
    response.stream_to_file("output.mp3")
    print("Audio saved to output.mp3")

text_to_speech_demo()
```

#### Using Ollama (Audio Limitations)

**Note**: Ollama does not currently provide built-in audio processing (speech-to-text or text-to-speech) like OpenAI's Whisper and TTS APIs. For audio processing with local models, you would need to use separate tools:

**For Speech-to-Text**, use OpenAI's open-source Whisper model:
```python
import whisper

# Load the Whisper model (downloads on first use)
model = whisper.load_model("base")

# Transcribe audio file
result = model.transcribe("audio.mp3")
print(result["text"])
```

**For Text-to-Speech**, use libraries like:
- `pyttsx3` for offline TTS
- `gTTS` (Google Text-to-Speech) 
- `coqui-tts` for neural TTS

For production applications requiring integrated audio processing, OpenAI's audio APIs provide a more seamless solution, while Ollama focuses on text and vision capabilities.

## Conclusion

You now have a comprehensive, practical understanding of the OpenAI API. You've moved from a simple "Hello, World!" to sophisticated patterns like function calling, streaming, and multimodal analysis.

You've learned:
-   The fundamental `chat.completions.create` call (OpenAI) and `ollama.chat()` (Ollama).
-   How to shape the AI's personality with **system messages** (works identically in both).
-   How to build stateful conversations by managing **message history** (same structure).
-   How to control output with `temperature` and `max_tokens`/`num_predict`.
-   How to create real-time experiences with **streaming** (both support it).
-   How to connect AI to the world with **function calling** (OpenAI native, Ollama via prompts).
-   How to work with images (both support vision) and audio (OpenAI native, Ollama requires separate tools).

These are the essential building blocks you will use in every AI application you create. Whether you choose cloud-based (OpenAI) or local (Ollama) models, the core patterns remain the same. You are now fully equipped to build your own intelligent systems with either provider.

# References and Further Reading

- OpenAI API Documentation. https://platform.openai.com/docs/
- Complete Guide to the OpenAI API 2025 (Zuplo). https://zuplo.com/blog/2025/04/10/openai-api
- OpenAI Responses API: A Comprehensive Guide. https://medium.com/@odhitom09/openai-responses-api-a-comprehensive-guide-ad546132b2ed
- What is OpenAI's API? How to Start Using It. https://latenode.com/blog/what-is-openais-api-how-to-start-using-it