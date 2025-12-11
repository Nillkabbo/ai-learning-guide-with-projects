"""
Globally-Scalable IoT Platform - Complete Solution
Chapter 20 Project

Demonstrates scaling patterns: queues, caching, and horizontal scaling.
"""

from fastapi import FastAPI
from typing import Dict
from datetime import datetime
import os
from dotenv import load_dotenv
from cachetools import TTLCache

app = FastAPI(title="Scalable IoT Platform")

load_dotenv()

# In-memory queue for demo (use Redis in production)
task_queue = []
task_results = {}

# Cache for frequently accessed data
cache = TTLCache(maxsize=1000, ttl=300)


@app.post("/tasks")
async def submit_task(task: Dict):
    """Submit task to queue."""
    task_id = f"task_{len(task_queue)}_{datetime.now().timestamp()}"
    task_item = {
        "task_id": task_id,
        "task": task,
        "status": "queued",
        "created_at": datetime.now().isoformat()
    }
    task_queue.append(task_item)
    task_results[task_id] = task_item
    
    # Simulate processing
    asyncio.create_task(process_task(task_id))
    
    return {"task_id": task_id, "status": "queued"}


async def process_task(task_id: str):
    """Process task asynchronously."""
    await asyncio.sleep(1)  # Simulate processing
    if task_id in task_results:
        task_results[task_id]["status"] = "completed"
        task_results[task_id]["completed_at"] = datetime.now().isoformat()


@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """Get task status."""
    # Check cache first
    if task_id in cache:
        return cache[task_id]
    
    # Get from results
    if task_id in task_results:
        result = task_results[task_id]
        cache[task_id] = result
        return result
    
    return {"error": "Task not found"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "queue_size": len(task_queue),
        "cache_size": len(cache)
    }


@app.get("/metrics")
async def get_metrics():
    """Get platform metrics."""
    return {
        "tasks_queued": len(task_queue),
        "tasks_completed": sum(1 for t in task_results.values() if t["status"] == "completed"),
        "cache_hits": len(cache),
        "cache_size": len(cache)
    }


if __name__ == "__main__":
    import uvicorn
    import asyncio
    uvicorn.run(app, host="0.0.0.0", port=8000)
