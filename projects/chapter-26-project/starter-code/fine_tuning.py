"""
Specialized IoT Diagnostic Assistant - Starter Code
Chapter 26 Project

This starter code provides a basic structure for fine-tuning a model
on IoT log classification data.
"""

import os
import json
from typing import List, Dict

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai


def prepare_training_data() -> List[Dict]:
    """
    Prepare fine-tuning dataset in JSONL format.
    
    Returns:
        List of training examples
    """
    # TODO: Create IoT log examples
    # TODO: Format as JSONL
    # TODO: Ensure quality
    examples = [
        {
            "messages": [
                {"role": "system", "content": "You are an IoT diagnostic assistant."},
                {"role": "user", "content": "TEMP_SENSOR: 95C STATUS:WARNING"},
                {"role": "assistant", "content": "Overheating detected. Check sensor calibration."}
            ]
        }
    ]
    return examples


def create_fine_tuning_job(training_file: str) -> str:
    """
    Create fine-tuning job.
    
    Args:
        training_file: Path to training file
        
    Returns:
        Job ID
    """
    # TODO: Upload training file
    # TODO: Create fine-tuning job
    # TODO: Return job ID
    return "ftjob_123"


def evaluate_model(model_id: str, test_data: List[Dict]) -> Dict:
    """
    Evaluate fine-tuned model.
    
    Args:
        model_id: Fine-tuned model ID
        test_data: Test dataset
        
    Returns:
        Evaluation results
    """
    # TODO: Test model on validation set
    # TODO: Compare to base model
    # TODO: Calculate metrics
    return {"accuracy": 0.95, "improvement": 0.10}


def main():
    """Main function."""
    print("🎯 Fine-Tuning IoT Diagnostic Assistant")
    print("This is a starter template for fine-tuning workflow.\n")
    
    # TODO: Prepare data
    # TODO: Create fine-tuning job
    # TODO: Monitor progress
    # TODO: Evaluate model


if __name__ == "__main__":
    main()
