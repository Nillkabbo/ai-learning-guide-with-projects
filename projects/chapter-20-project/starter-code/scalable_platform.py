"""
Globally-Scalable IoT Platform - Starter Code
Chapter 20 Project

This starter code provides a basic structure for building a scalable platform
with horizontal scaling, queues, and database optimization.
"""

from fastapi import FastAPI
from typing import Dict
import asyncio

# TODO: Import required libraries
# import redis
# from sqlalchemy import create_engine
# from cachetools import TTLCache

app = FastAPI()

# TODO: Initialize queue
# task_queue = None

# TODO: Initialize cache
# cache = TTLCache(maxsize=1000, ttl=300)


@app.post("/tasks")
async def submit_task(task: Dict):
    """Submit task to queue."""
    # TODO: Add task to queue
    # TODO: Return task ID
    return {"task_id": "TODO", "status": "queued"}


@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """Get task status."""
    # TODO: Check task status
    # TODO: Return status
    return {"task_id": task_id, "status": "TODO"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
