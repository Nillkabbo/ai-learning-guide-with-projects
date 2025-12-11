"""
Safe IoT Assistant - Starter Code
Chapter 4 Project

This starter code provides a basic structure for building a safe AI assistant
that implements safeguards from Chapter 4.
"""

import os
from typing import Dict, Tuple

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai


def classify_question(question: str) -> str:
    """
    Classify a question to determine appropriate handling.
    
    Args:
        question: The user's question
        
    Returns:
        Classification: 'math', 'realtime', or 'general'
    """
    # TODO: Implement classification logic
    # Check for math keywords and numbers
    # Check for real-time information requests
    # Default to general
    return "general"


def handle_math_question(question: str) -> Tuple[str, str]:
    """
    Handle math questions safely by generating code.
    
    Args:
        question: The math question
        
    Returns:
        Tuple of (code, explanation)
    """
    # TODO: Use AI to generate Python code for the math problem
    # TODO: Return code and explanation
    # WARNING: Never execute code directly from AI without validation!
    return ("# TODO: Generated code", "TODO: Explanation")


def get_confidence_score(response: str) -> int:
    """
    Extract confidence score from AI response.
    
    Args:
        response: AI response that should include confidence
        
    Returns:
        Confidence score (1-10)
    """
    # TODO: Parse confidence from response
    # Look for "Confidence: X" pattern
    return 5  # Default


def verify_claims(response: str) -> list:
    """
    Identify factual claims that need verification.
    
    Args:
        response: AI response to check
        
    Returns:
        List of claims that need verification
    """
    # TODO: Use AI to identify factual claims
    # TODO: Return list of claims needing verification
    return []


class SafeAssistant:
    """Safe AI assistant with safeguards."""
    
    def __init__(self):
        """Initialize the safe assistant."""
        # TODO: Load environment variables
        # TODO: Initialize OpenAI client
        # TODO: Set up system message requesting confidence scores
        pass
    
    def answer(self, question: str) -> Dict:
        """
        Answer a question with appropriate safeguards.
        
        Args:
            question: User's question
            
        Returns:
            Dictionary with answer, confidence, and verification info
        """
        # TODO: Classify the question
        # TODO: Route to appropriate handler
        # TODO: Get confidence score
        # TODO: Identify claims needing verification
        # TODO: Return structured response
        
        return {
            "answer": "TODO: AI response",
            "confidence": 5,
            "needs_verification": [],
            "question_type": "general"
        }


def main():
    """Main function to run the safe assistant."""
    print("🛡️  Safe IoT Assistant")
    print("Type 'quit' to exit\n")
    
    # TODO: Initialize assistant
    # assistant = SafeAssistant()
    
    while True:
        try:
            question = input("Question: ").strip()
            
            if question.lower() in ['quit', 'exit']:
                break
            
            # TODO: Get safe answer
            # result = assistant.answer(question)
            # TODO: Display result with safeguards
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
