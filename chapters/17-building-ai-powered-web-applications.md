# Chapter 17: Building AI-Powered Web Applications with Python

So far, our AI agents and models have lived primarily in scripts and command-line interfaces. While powerful, this isn't how most people interact with software. To deliver the value of your AI to a broad audience, you need to make it accessible. The most universal way to do that is through a web application.

Think of your AI model as a car's engine—it's the core component that provides the power. A web application is the dashboard, steering wheel, and pedals. It's the interface that allows a user to control the engine without needing to understand its internal mechanics. This chapter is about building that dashboard.

We will learn how to wrap our AI capabilities in web APIs, creating endpoints that can be accessed from any browser or client application. We'll start with the basics and progressively build up to a full-featured, real-time IoT device management interface.

### Learning Objectives

By the end of this chapter, you will be able to:

-   Build web APIs that serve AI model responses using Flask and FastAPI.
-   Handle file uploads for images, audio, and PDFs in your AI applications.
-   Implement streaming responses for real-time, interactive AI experiences.
-   Use Server-Sent Events (SSE) to push live updates from your AI to a web client.
-   Validate API inputs and outputs with Pydantic for robust, type-safe applications.
-   Create a complete, AI-powered IoT device management web interface from scratch.

## Your First AI API: From Script to Service

Let's take the simplest possible AI task—answering a question—and expose it as a web service. We'll start with Flask, a wonderfully simple framework perfect for understanding the core concepts.

### Flask: A Simple and Direct Approach

Flask is known for its minimalism, which makes it an excellent teaching tool. Our goal is to create an endpoint at `/ask` that accepts a question in a JSON request and returns an AI-generated answer.

First, let's set up the basic Flask application and route.

#### Using OpenAI

```python
from flask import Flask, request, jsonify
import openai

# 1. Create a Flask application instance
app = Flask(__name__)

# 2. Initialize the OpenAI client
# Assumes the OPENAI_API_KEY environment variable is set
client = openai.OpenAI()

# 3. Define an endpoint using a route decorator
@app.route('/ask', methods=['POST'])
def ask_ai():
    # 1. Get the JSON data from the incoming request
    data = request.get_json()
    if not data or 'question' not in data:
        # Return an error if the request is malformed
        return jsonify({'error': 'JSON payload must include a "question" key.'}), 400

    question = data['question']

    # 2. Call the OpenAI API
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}]
        )
        answer = response.choices[0].message.content
    except Exception as e:
        # Handle potential API errors
        return jsonify({'error': f'AI service error: {str(e)}'}), 503

    # 3. Return the AI's answer in a JSON response
    return jsonify({
        'question': question,
        'answer': answer
    })

# 4. A standard block to run the app when the script is executed
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

#### Using Ollama

```python
from flask import Flask, request, jsonify
import ollama

# 1. Create a Flask application instance
app = Flask(__name__)

# 2. Configure Ollama model (default can be overridden via environment variable)
import os
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama2')

# 3. Define an endpoint using a route decorator
@app.route('/ask', methods=['POST'])
def ask_ai():
    # 1. Get the JSON data from the incoming request
    data = request.get_json()
    if not data or 'question' not in data:
        # Return an error if the request is malformed
        return jsonify({'error': 'JSON payload must include a "question" key.'}), 400

    question = data['question']
    
    # Optional: Allow model override in request
    model = data.get('model', OLLAMA_MODEL)

    # 2. Call the Ollama API
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": question}]
        )
        answer = response["message"]["content"]
    except Exception as e:
        # Handle potential API errors (e.g., Ollama not running, model not found)
        return jsonify({'error': f'AI service error: {str(e)}'}), 503

    # 3. Return the AI's answer in a JSON response
    return jsonify({
        'question': question,
        'answer': answer,
        'model': model
    })

# 4. A standard block to run the app when the script is executed
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**Note**: Make sure Ollama is running (`ollama serve`) and the model is pulled (`ollama pull llama2`) before starting the Flask server.

This skeleton sets up a web server. The `@app.route('/ask', methods=['POST'])` decorator tells Flask that whenever a `POST` request comes to the `/ask` URL, it should run the `ask_ai` function.

With the complete code in a file named `app.py`, you can run it:

```bash
# Start the Flask development server
python app.py
```

In another terminal, you can test your new AI endpoint using `curl`:

```bash
curl -X POST http://localhost:5000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "What is the primary function of an IoT actuator?"}'
```

You've just built your first AI-powered web service! While simple, it contains all the fundamental pieces: receiving a request, processing it with an AI, and returning a structured response.

## Graduating to FastAPI: Speed and Safety

Flask is great for simple projects, but for production APIs, the modern choice is **FastAPI**. It offers several key advantages:

-   **Speed:** It's one of the fastest Python web frameworks available.
-   **Type Safety:** It uses Python's type hints and a library called Pydantic to validate incoming data automatically.
-   **Automatic Docs:** It generates interactive API documentation (like Swagger UI) for you, which is invaluable for development.
-   **Async Support:** It's built from the ground up to support asynchronous operations, which is perfect for handling long-running AI tasks without blocking the server.

Let's rebuild our `/ask` endpoint in FastAPI.

### Pydantic: Your Data's Bodyguard

First, we define the *shape* of our expected request and response data using Pydantic models. This is like creating a contract for our API.

```python
from pydantic import BaseModel, Field
from typing import Optional

# Pydantic models define the structure and types of our API data.
# This ensures that any data sent to our endpoint matches this structure.

class AIRequest(BaseModel):
    question: str = Field(
        ..., 
        min_length=10, 
        max_length=500,
        description="The question to ask the AI."
    )

class AIResponse(BaseModel):
    question: str
    answer: str
    tokens_used: Optional[int] = None
```

These models enforce that every request to `/ai/ask` *must* have a `question` field that is a string between 10 and 500 characters long. FastAPI handles the validation and error responses for us automatically.

### Building the FastAPI Endpoint

Now, we create the FastAPI application and endpoint. Notice how we use the Pydantic models as type hints in the function signature.

#### Using OpenAI

```python
from fastapi import FastAPI, HTTPException
from datetime import datetime
import openai

# 1. Create a FastAPI application instance
app = FastAPI(
    title="Simple AI API",
    description="A demonstration of a production-ready AI endpoint.",
    version="1.0.0"
)

# Initialize OpenAI client
client = openai.OpenAI()

# 2. Define the endpoint using the Pydantic models
@app.post("/ai/ask", response_model=AIResponse)
async def ask_ai(request: AIRequest):
    """Receives a question and returns an AI-generated answer."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": request.question}]
        )
        
        answer = response.choices[0].message.content
        tokens = response.usage.total_tokens if response.usage else None
        
        return AIResponse(
            question=request.question,
            answer=answer,
            tokens_used=tokens
        )
        
    except Exception as e:
        # FastAPI's HTTPException is the standard way to return error responses.
        raise HTTPException(
            status_code=503, 
            detail=f"AI service error: {str(e)}"
        )
```

#### Using Ollama

```python
from fastapi import FastAPI, HTTPException
from datetime import datetime
import ollama
import os

# 1. Create a FastAPI application instance
app = FastAPI(
    title="Simple AI API",
    description="A demonstration of a production-ready AI endpoint.",
    version="1.0.0"
)

# Configure default model
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama2')

# 2. Define the endpoint using the Pydantic models
@app.post("/ai/ask", response_model=AIResponse)
async def ask_ai(request: AIRequest):
    """Receives a question and returns an AI-generated answer."""
    
    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": request.question}]
        )
        
        answer = response["message"]["content"]
        # Ollama doesn't provide token usage in the same way, so we set it to None
        tokens = None
        
        return AIResponse(
            question=request.question,
            answer=answer,
            tokens_used=tokens
        )
        
    except Exception as e:
        # FastAPI's HTTPException is the standard way to return error responses.
        raise HTTPException(
            status_code=503, 
            detail=f"AI service error: {str(e)}"
        )
```

To run this, save it as `main.py` and use `uvicorn`, a high-performance server:

```bash
uvicorn main:app --reload
```

Now, navigate to `http://127.0.0.1:8000/docs` in your browser. You'll see beautiful, interactive API documentation that FastAPI generated automatically from your code and Pydantic models. This is a massive productivity boost.

## Streaming Responses for a Real-Time Feel

Waiting for an AI to generate a long piece of text can be a poor user experience. The solution is **streaming**, where the server sends the response back to the client word-by-word as it's generated.

FastAPI makes this incredibly elegant with its `StreamingResponse` and support for async generators.

First, we need a function that `yields` the AI's response in chunks. We do this by setting `stream=True` in the OpenAI API call.

#### Using OpenAI

```python
import asyncio
from typing import AsyncGenerator
import openai

client = openai.OpenAI()

async def generate_streaming_response(prompt: str) -> AsyncGenerator[str, None]:
    """Calls the OpenAI API in streaming mode and yields content chunks."""
    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        
        # Iterate over the stream of chunks
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content
                await asyncio.sleep(0.01) # Small delay to simulate network flow
    except Exception as e:
        print(f"Error during stream generation: {e}")
        yield f"An error occurred: {str(e)}"
```

#### Using Ollama

```python
import asyncio
from typing import AsyncGenerator
import ollama
import os

OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama2')

async def generate_streaming_response(prompt: str) -> AsyncGenerator[str, None]:
    """Calls the Ollama API in streaming mode and yields content chunks."""
    try:
        stream = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        
        # Iterate over the stream of chunks
        for chunk in stream:
            content = chunk.get("message", {}).get("content", "")
            if content:
                yield content
                await asyncio.sleep(0.01)  # Small delay to simulate network flow
    except Exception as e:
        print(f"Error during stream generation: {e}")
        yield f"An error occurred: {str(e)}"
```

Now, we create an endpoint that returns a `StreamingResponse`, passing our generator function to it.

#### Using OpenAI

```python
from fastapi.responses import StreamingResponse

@app.post("/ai/stream")
async def stream_ai_analysis(request: AIRequest):
    """Streams a detailed AI analysis token-by-token."""
    prompt = f"Provide a detailed, multi-paragraph analysis of the following topic: {request.question}"
    return StreamingResponse(
        generate_streaming_response(prompt), 
        media_type="text/plain"
    )
```

#### Using Ollama

```python
from fastapi.responses import StreamingResponse

@app.post("/ai/stream")
async def stream_ai_analysis(request: AIRequest):
    """Streams a detailed AI analysis token-by-token."""
    prompt = f"Provide a detailed, multi-paragraph analysis of the following topic: {request.question}"
    return StreamingResponse(
        generate_streaming_response(prompt), 
        media_type="text/plain"
    )
```

**Note**: Ollama's streaming API works similarly to OpenAI's. Both support streaming responses for real-time user experiences.

A client (like a JavaScript frontend) can use the `fetch` API to read this stream and update the UI in real time, creating the familiar "typing" effect seen in tools like ChatGPT.

## Pushing Live Updates with Server-Sent Events (SSE)

While streaming is great for a single, long response, **Server-Sent Events (SSE)** are designed for pushing a sequence of *distinct events* from the server to the client over a long-lived connection. This is perfect for a live monitoring dashboard where you want to send status updates, alerts, and AI insights as they happen.

FastAPI can handle SSE using the `sse-starlette` library.

First, let's create an async generator that simulates monitoring an IoT device. It will periodically `yield` structured event data.

```python
import random

async def device_event_generator() -> AsyncGenerator[dict, None]:
    """Generates simulated device status events indefinitely."""
    while True:
        # Simulate a random device update
        device_id = f"sensor_{random.randint(1, 5)}"
        temp = round(70 + random.uniform(-5, 10), 1)
        
        # Check if an alert condition is met
        if temp > 80:
            event_type = "alert"
            message = f"Critical temperature detected: {temp}°F"
        else:
            event_type = "update"
            message = "Status normal"
        
        # Yield the event in the format required by sse-starlette
        yield {
            "event": event_type,
            "data": json.dumps({
                "device_id": device_id,
                "temperature": temp,
                "message": message,
                "timestamp": datetime.now().isoformat()
            })
        }
        
        await asyncio.sleep(2) # Wait 2 seconds before the next event
```

Next, we create an SSE endpoint that returns an `EventSourceResponse`.

```python
from sse_starlette.sse import EventSourceResponse

@app.get("/events/devices")
async def device_event_stream():
    """An SSE endpoint that pushes live device events to clients."""
    return EventSourceResponse(device_event_generator())
```

A simple HTML page with a few lines of JavaScript can connect to this endpoint and display a live feed of events.

```html
<!-- client.html -->
<h1>Live IoT Device Feed</h1>
<div id="events"></div>

<script>
    const eventLog = document.getElementById('events');
    // The browser's built-in EventSource API handles the connection.
    const source = new EventSource('/events/devices');

    // Listen for custom 'alert' events
    source.addEventListener('alert', function(event) {
        const data = JSON.parse(event.data);
        const div = document.createElement('div');
        div.style.color = 'red';
        div.textContent = `ALERT: ${data.device_id} - ${data.message}`;
        eventLog.appendChild(div);
    });

    // Listen for custom 'update' events
    source.addEventListener('update', function(event) {
        const data = JSON.parse(event.data);
        const div = document.createElement('div');
        div.textContent = `UPDATE: ${data.device_id} reports temp ${data.temperature}°F.`;
        eventLog.appendChild(div);
    });
</script>
```

This pattern is incredibly powerful for building dynamic, real-time dashboards that are augmented with AI insights pushed directly from the server.

## Handling File Uploads for Multimodal AI

Modern AI is multimodal. It can understand images, audio, and documents. A production application must be able to handle file uploads securely and efficiently.

FastAPI makes this easy with the `UploadFile` type. Let's create an endpoint that accepts an image and uses a vision model to analyze it.

#### Using OpenAI

```python
from fastapi import File, UploadFile, HTTPException
import base64
import openai

client = openai.OpenAI()

@app.post("/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    """Accepts an image, sends it to a vision model for analysis."""
    
    # 1. Read the file content into memory
    contents = await file.read()
    
    # 2. Validate file type and size (important for security)
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image type.")
    if len(contents) > 10 * 1024 * 1024: # 10 MB limit
        raise HTTPException(status_code=413, detail="File size exceeds 10MB limit.")

    # 3. Encode the image for the API call
    base64_image = base64.b64encode(contents).decode('utf-8')
    
    # 4. Call the vision model
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image. If it contains industrial equipment, identify any visible issues."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        }]
    )
    
    return {
        "filename": file.filename,
        "analysis": response.choices[0].message.content
    }
```

#### Using Ollama

```python
from fastapi import File, UploadFile, HTTPException
import base64
import ollama
import os

OLLAMA_MODEL = os.getenv('OLLAMA_VISION_MODEL', 'llava')  # Use vision-capable model

@app.post("/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    """Accepts an image, sends it to a vision model for analysis."""
    
    # 1. Read the file content into memory
    contents = await file.read()
    
    # 2. Validate file type and size (important for security)
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image type.")
    if len(contents) > 10 * 1024 * 1024: # 10 MB limit
        raise HTTPException(status_code=413, detail="File size exceeds 10MB limit.")

    # 3. Encode the image for the API call
    base64_image = base64.b64encode(contents).decode('utf-8')
    
    # 4. Call the vision model (Ollama vision models use different API structure)
    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{
                "role": "user",
                "content": "Describe this image. If it contains industrial equipment, identify any visible issues.",
                "images": [base64_image]  # Ollama uses 'images' array
            }]
        )
        
        return {
            "filename": file.filename,
            "analysis": response["message"]["content"]
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Vision model error: {str(e)}. Make sure you have a vision-capable model like 'llava' installed."
        )
```

**Note**: For vision capabilities with Ollama, you need to install a vision-capable model like `llava` (`ollama pull llava`). Vision support varies by model, so check Ollama's documentation for available vision models.

The same pattern applies to other file types. For audio, you might use OpenAI's Whisper model for transcription. For PDFs, you would use a library like `PyPDF2` to extract text before sending it to an LLM for summarization or analysis.

## Putting It All Together: A Live IoT Dashboard

Let's combine these concepts—FastAPI, WebSockets (an alternative to SSE for two-way communication), Pydantic, and AI—to create a complete, interactive web dashboard for managing IoT devices.

Our system will have:
-   A FastAPI backend.
-   A WebSocket endpoint at `/ws` for real-time, bidirectional communication.
-   A simple HTML/JavaScript frontend that connects to the WebSocket.
-   AI-powered diagnostics and a chat assistant.

```python
# A complete app.py for our IoT Dashboard

# ... (imports: FastAPI, WebSocket, etc.)

app = FastAPI()
manager = ConnectionManager() # A class to manage WebSocket connections

# ... (In-memory storage for devices, alerts) ...

@app.get("/", response_class=HTMLResponse)
async def get_dashboard():
    # Returns the HTML for the frontend page
    # (The full HTML is provided in the chapter's source code)
    return HTMLResponse(content="...")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Wait for a message from the client (e.g., a button click)
            data = await websocket.receive_json()
            action = data.get("action")

            if action == "diagnose_device":
                # AI-powered diagnostics
                device_id = data.get("device_id")
                # ... build prompt for the specific device ...
                
                # Using OpenAI:
                # response = client.chat.completions.create(
                #     model="gpt-4o-mini",
                #     messages=[{"role": "user", "content": prompt}]
                # )
                # diagnosis = response.choices[0].message.content
                
                # Using Ollama:
                # response = ollama.chat(
                #     model="llama3.2",
                #     messages=[{"role": "user", "content": prompt}]
                # )
                # diagnosis = response["message"]["content"]
                
                diagnosis = "AI analysis result..."
                
                # Broadcast the new alert to all connected clients
                await manager.broadcast({
                    "type": "new_alert",
                    "alert": {"device_id": device_id, "message": diagnosis}
                })

            elif action == "chat":
                # AI chat assistant logic
                user_message = data.get("message")
                # ... build context with current device states ...
                
                # Using OpenAI:
                # response = client.chat.completions.create(
                #     model="gpt-4o-mini",
                #     messages=[{"role": "user", "content": user_message}]
                # )
                # ai_response = response.choices[0].message.content
                
                # Using Ollama:
                # response = ollama.chat(
                #     model="llama3.2",
                #     messages=[{"role": "user", "content": user_message}]
                # )
                # ai_response = response["message"]["content"]
                
                ai_response = "AI assistant response..."
                
                # Send the response back to the specific client who asked
                await websocket.send_json({
                    "type": "ai_response",
                    "message": ai_response
                })

    except WebSocketDisconnect:
        manager.disconnect(websocket)

# ... (Background task to simulate device status changes and broadcast updates) ...
```

This architecture creates a powerful, dynamic user experience. The dashboard loads, connects to the WebSocket, and receives an initial list of devices. A background task on the server simulates device activity, and whenever a device's status changes, the `manager.broadcast` function pushes the update to *every connected user's screen* in real time. When a user clicks "Diagnose," a message is sent to the server, an AI diagnosis is performed, and the resulting alert is broadcast back to everyone. This is the blueprint for modern, AI-augmented applications.

# References and Further Reading

- How to Build an AI App: A Step-by-Step Guide (Vercel): https://vercel.com/guides/how-to-build-ai-app
- How to Implement AI in Web Development: A Practical Guide with Real-Life Examples (DEV.to): https://dev.to/ansif_branding_84cec990b812/how-to-implement-ai-in-web-development-a-practical-guide-with-real-life-examples-4ljc
- AI-Powered Web Applications: Building the Future with Django and TensorFlow (Medium): https://medium.com/@tarekeesa7/ai-powered-web-applications-building-the-future-with-django-and-tensorflow-4e71e83c0885
- Building AI Applications on the Web (Manning): https://www.manning.com/books/building-ai-applications-on-the-web
- Build a Local and Offline-Capable Chatbot with WebLLM (web.dev): https://web.dev/articles/ai-chatbot-webllm