"""
IoT Firmware Update System - Complete Solution
Chapter 25 Project

Demonstrates DevOps: containerization concepts, feature flags, deployment, rollback.
"""

from fastapi import FastAPI
from typing import Dict
import os
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

app = FastAPI(title="IoT Firmware Update System")

load_dotenv()

# Feature flags
FEATURE_FLAGS = {
    "new_model": os.getenv("FEATURE_NEW_MODEL", "false").lower() == "true",
    "beta_features": os.getenv("FEATURE_BETA", "false").lower() == "true"
}

# Deployment state
deployment_state = {
    "current_version": "v1.0.0",
    "previous_version": None,
    "deployment_status": "stable"
}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": deployment_state["current_version"],
        "features": FEATURE_FLAGS
    }


@app.post("/deploy")
async def deploy_firmware(firmware: Dict):
    """Deploy firmware update."""
    new_version = firmware.get("version", "v1.0.1")
    
    # Store previous version for rollback
    deployment_state["previous_version"] = deployment_state["current_version"]
    deployment_state["current_version"] = new_version
    deployment_state["deployment_status"] = "deploying"
    
    # Simulate deployment
    # In production: actual deployment logic here
    
    deployment_state["deployment_status"] = "deployed"
    
    return {
        "status": "deployed",
        "version": new_version,
        "previous_version": deployment_state["previous_version"]
    }


@app.post("/rollback")
async def rollback():
    """Rollback to previous version."""
    if not deployment_state["previous_version"]:
        return {"error": "No previous version to rollback to"}
    
    # Rollback
    deployment_state["current_version"] = deployment_state["previous_version"]
    deployment_state["deployment_status"] = "rolled_back"
    
    return {
        "status": "rolled_back",
        "version": deployment_state["current_version"]
    }


@app.get("/features")
async def get_features():
    """Get feature flags."""
    return FEATURE_FLAGS


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
