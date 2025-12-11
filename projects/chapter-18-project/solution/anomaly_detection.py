"""
Real-Time IoT Anomaly Detection System - Complete Solution
Chapter 18 Project

Demonstrates WebSockets, background workers, and real-time processing.
"""

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio
import os
from dotenv import load_dotenv
from cachetools import TTLCache

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

app = FastAPI(title="IoT Anomaly Detection")

load_dotenv()

if OPENAI_AVAILABLE:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        client = openai.OpenAI(api_key=api_key)
    else:
        client = None
else:
    client = None

# Cache for anomaly detection results
cache = TTLCache(maxsize=100, ttl=300)

# Connected WebSocket clients
connected_clients = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time updates."""
    await websocket.accept()
    connected_clients.append(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            
            # Check cache
            if data in cache:
                result = cache[data]
            else:
                # Detect anomaly using AI
                if client:
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[{
                                "role": "user",
                                "content": f"Analyze this IoT sensor data for anomalies: {data}"
                            }]
                        )
                        result = response.choices[0].message.content
                        cache[data] = result
                    except Exception as e:
                        result = f"Error: {str(e)}"
                else:
                    result = "AI client not available"
            
            await websocket.send_json({
                "data": data,
                "analysis": result,
                "anomaly_detected": "anomaly" in result.lower() or "unusual" in result.lower()
            })
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        if websocket in connected_clients:
            connected_clients.remove(websocket)


async def background_worker():
    """Background worker for periodic monitoring."""
    while True:
        await asyncio.sleep(5)
        # Simulate periodic checks
        for client in connected_clients:
            try:
                await client.send_json({
                    "type": "heartbeat",
                    "status": "monitoring"
                })
            except:
                pass


@app.get("/")
async def root():
    """Root endpoint with WebSocket test page."""
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>IoT Anomaly Detection</title></head>
    <body>
        <h1>Real-Time Anomaly Detection</h1>
        <input type="text" id="dataInput" placeholder="Enter sensor data">
        <button onclick="sendData()">Send</button>
        <div id="messages"></div>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                document.getElementById("messages").innerHTML += 
                    JSON.stringify(data, null, 2) + "<br>";
            };
            function sendData() {
                const input = document.getElementById("dataInput");
                ws.send(input.value);
                input.value = "";
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.on_event("startup")
async def startup_event():
    """Start background worker on startup."""
    asyncio.create_task(background_worker())


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
