"""
AI-Powered IoT Dashboard - Complete Solution
Chapter 17 Project

Demonstrates web application with FastAPI, file uploads, and streaming.
"""

import os
import io
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

app = FastAPI(title="IoT Dashboard API")

load_dotenv()

if OPENAI_AVAILABLE:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        client = openai.OpenAI(api_key=api_key)
    else:
        client = None
else:
    client = None


class DeviceStatus(BaseModel):
    """Device status model."""
    device_id: str
    status: str


# Mock device storage
devices = {}


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "IoT Dashboard API", "status": "running"}


@app.post("/devices/{device_id}/status")
async def update_status(device_id: str, status: DeviceStatus):
    """Update device status."""
    devices[device_id] = status.dict()
    return {"status": "updated", "device": devices[device_id]}


@app.get("/devices")
async def list_devices():
    """List all devices."""
    return {"devices": devices}


@app.post("/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    """Analyze uploaded device image."""
    if not client:
        return {"error": "OpenAI client not available"}
    
    # Read file
    contents = await file.read()
    
    # Use OpenAI vision
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this IoT device image for issues."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{contents.hex()}"}}
                ]
            }]
        )
        analysis = response.choices[0].message.content
        return {"analysis": analysis}
    except Exception as e:
        return {"error": str(e)}


@app.get("/stream/status")
async def stream_status():
    """Stream device status updates."""
    async def generate():
        import asyncio
        for i in range(5):
            yield f"data: {{'cycle': {i+1}, 'status': 'monitoring'}}\n\n"
            await asyncio.sleep(1)
    
    return StreamingResponse(generate(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
