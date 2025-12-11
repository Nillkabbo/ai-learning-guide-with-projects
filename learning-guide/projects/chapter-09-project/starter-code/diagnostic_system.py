"""
Smart IoT Diagnostic System - Starter Code
Chapter 9 Project

This starter code provides a basic structure for building a diagnostic system
using all fundamental prompt engineering patterns.
"""

import os
from typing import Dict, List

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai


# Few-shot examples for diagnostic patterns
FEW_SHOT_EXAMPLES = [
    # TODO: Add few-shot examples
    {
        "input": "Device: TEMP_SENSOR_01, Status: WARNING, Reading: 95C",
        "output": "Issue: Overheating. Cause: Possible sensor malfunction or environmental heat. Solution: Check sensor calibration, verify ambient temperature."
    }
]


def zero_shot_diagnosis(device_status: str) -> str:
    """
    Diagnose using zero-shot prompting.
    
    Args:
        device_status: Device status message
        
    Returns:
        Diagnosis
    """
    # TODO: Implement zero-shot prompt
    return "TODO: Zero-shot diagnosis"


def few_shot_diagnosis(device_status: str) -> str:
    """
    Diagnose using few-shot prompting.
    
    Args:
        device_status: Device status message
        
    Returns:
        Diagnosis
    """
    # TODO: Implement few-shot prompt with examples
    return "TODO: Few-shot diagnosis"


def chain_of_thought_diagnosis(device_status: str) -> str:
    """
    Diagnose using chain-of-thought reasoning.
    
    Args:
        device_status: Device status message
        
    Returns:
        Diagnosis with reasoning steps
    """
    # TODO: Implement chain-of-thought prompt
    return "TODO: Chain-of-thought diagnosis"


def role_based_diagnosis(device_status: str) -> str:
    """
    Diagnose using role-based expert persona.
    
    Args:
        device_status: Device status message
        
    Returns:
        Expert diagnosis
    """
    # TODO: Implement role-based prompt (IoT expert)
    return "TODO: Role-based diagnosis"


class DiagnosticSystem:
    """Smart diagnostic system using prompt engineering."""
    
    def __init__(self):
        """Initialize diagnostic system."""
        # TODO: Load environment variables
        # TODO: Initialize OpenAI client
        pass
    
    def diagnose(self, device_status: str, method: str = "zero_shot") -> Dict:
        """
        Diagnose device issue using specified method.
        
        Args:
            device_status: Device status message
            method: Prompting method (zero_shot, few_shot, chain_of_thought, role_based)
            
        Returns:
            Diagnosis results
        """
        # TODO: Route to appropriate method
        # TODO: Return structured diagnosis
        return {"method": method, "diagnosis": "TODO"}


def main():
    """Main function."""
    print("🔍 Smart Diagnostic System")
    print("Type 'quit' to exit\n")
    
    # TODO: Initialize system
    # system = DiagnosticSystem()
    
    # TODO: Implement main loop with method selection


if __name__ == "__main__":
    main()
