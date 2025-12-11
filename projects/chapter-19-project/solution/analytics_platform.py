"""
IoT Analytics Platform - Complete Solution
Chapter 19 Project

Demonstrates event-driven architecture and polyglot persistence patterns.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
from datetime import datetime
import os
from dotenv import load_dotenv

app = FastAPI(title="IoT Analytics Platform")

load_dotenv()

# In-memory storage for demo (replace with real databases in production)
events_store = []
analytics_store = {}


class Event(BaseModel):
    """Event model."""
    event_type: str
    data: Dict
    timestamp: str = None
    
    def __init__(self, **data):
        if 'timestamp' not in data:
            data['timestamp'] = datetime.now().isoformat()
        super().__init__(**data)


@app.post("/events")
async def ingest_event(event: Event):
    """Ingest event into system."""
    events_store.append(event.dict())
    
    # Update analytics
    event_type = event.event_type
    if event_type not in analytics_store:
        analytics_store[event_type] = 0
    analytics_store[event_type] += 1
    
    return {"status": "ingested", "event_id": len(events_store)}


@app.get("/analytics")
async def get_analytics():
    """Get analytics data."""
    return {
        "total_events": len(events_store),
        "events_by_type": analytics_store,
        "recent_events": events_store[-10:] if events_store else []
    }


@app.get("/events")
async def list_events(limit: int = 100):
    """List recent events."""
    return {"events": events_store[-limit:]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
