"""
Domain-Specific IoT Troubleshooting System - Starter Code
Chapter 12 Project

This starter code provides a basic structure for building a domain-specific
troubleshooting system with expert personas and domain knowledge.
"""

import os
from typing import Dict, List

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai


# Domain knowledge base
DOMAIN_KNOWLEDGE = {
    "common_issues": [
        "Temperature sensors: Check calibration, verify ambient conditions",
        "Connectivity: Verify network settings, check signal strength",
        # TODO: Add more domain-specific knowledge
    ],
    "terminology": {
        "MQTT": "Message Queuing Telemetry Transport protocol",
        "CoAP": "Constrained Application Protocol",
        # TODO: Add more IoT terminology
    }
}


def create_expert_persona() -> str:
    """
    Create domain expert persona prompt.
    
    Returns:
        System prompt for IoT expert
    """
    # TODO: Create detailed expert persona
    # Include: years of experience, specialization, domain knowledge
    return "You are an IoT engineering expert..."


def diagnose_issue(device_status: str, client) -> str:
    """
    Diagnose device issue using domain expertise.
    
    Args:
        device_status: Device status message
        client: OpenAI client
        
    Returns:
        Domain-specific diagnosis
    """
    # TODO: Use expert persona
    # TODO: Include domain knowledge in context
    # TODO: Generate domain-appropriate solution
    return "TODO: Diagnosis"


def main():
    """Main function."""
    print("🔧 Domain-Specific IoT Troubleshooting")
    print("Type 'quit' to exit\n")
    
    # TODO: Initialize client
    # TODO: Implement main loop


if __name__ == "__main__":
    main()
