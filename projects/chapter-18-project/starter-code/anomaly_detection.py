"""
Real-Time IoT Anomaly Detection System - Starter Code
Chapter 18 Project

This starter code provides a basic structure for building a real-time
anomaly detection system with WebSockets and background workers.
"""

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio

# TODO: Import required libraries
# import openai
# from cachetools import TTLCache

app = FastAPI()

# TODO: Initialize cache
# cache = TTLCache(maxsize=100, ttl=300)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time updates."""
    await websocket.accept()
    # TODO: Implement WebSocket communication
    # TODO: Send real-time updates
    try:
        while True:
            data = await websocket.receive_text()
            # TODO: Process data
            # TODO: Detect anomalies
            # TODO: Send alerts
            await websocket.send_text(f"Echo: {data}")
    except Exception as e:
        print(f"WebSocket error: {e}")


async def background_worker():
    """Background worker for AI processing."""
    # TODO: Implement background processing
    # TODO: Use Celery or asyncio
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
        <div id="messages"></div>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = (event) => {
                document.getElementById("messages").innerHTML += event.data + "<br>";
            };
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
