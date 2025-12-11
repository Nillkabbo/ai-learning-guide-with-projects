"""
Safe IoT Assistant - Complete Solution
Chapter 4 Project

This solution demonstrates implementing safeguards for safe AI use:
- Question classification
- Safe math handling
- Confidence scoring
- Verification layers
"""

import os
import re
from typing import Dict, List, Tuple
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


def classify_question(question: str) -> str:
    """
    Classify a question to determine appropriate handling.
    
    Args:
        question: The user's question
        
    Returns:
        Classification: 'math', 'realtime', or 'general'
    """
    question_lower = question.lower()
    
    # Check for math indicators
    math_keywords = ['calculate', 'compute', 'solve', 'what is', 'how much', '+', '-', '*', '/']
    has_numbers = any(char.isdigit() for char in question)
    
    if any(keyword in question_lower for keyword in math_keywords) and has_numbers:
        return 'math'
    
    # Check for real-time information requests
    realtime_keywords = ['current', 'now', 'today', 'latest', 'recent', 'what time', 'what date']
    if any(keyword in question_lower for keyword in realtime_keywords):
        return 'realtime'
    
    return 'general'


def handle_math_question(question: str, client) -> Tuple[str, str]:
    """
    Handle math questions safely by generating code.
    
    Args:
        question: The math question
        client: OpenAI client
        
    Returns:
        Tuple of (code, explanation)
    """
    prompt = f"""Convert this math problem into Python code that can solve it:
    
    Problem: {question}
    
    Return ONLY valid Python code (no explanations). The code should:
    1. Define any variables needed
    2. Perform the calculation
    3. Print the result
    
    Code:"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        code = response.choices[0].message.content.strip()
        
        # Extract code block if present
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()
        elif "```" in code:
            code = code.split("```")[1].split("```")[0].strip()
        
        explanation = f"Generated Python code to solve: {question}"
        return code, explanation
    except Exception as e:
        return f"# Error generating code: {str(e)}", "Error"


def get_confidence_score(response: str) -> int:
    """
    Extract confidence score from AI response.
    
    Args:
        response: AI response that should include confidence
        
    Returns:
        Confidence score (1-10), default 5 if not found
    """
    # Look for "Confidence: X" pattern
    pattern = r'[Cc]onfidence[:\s]+(\d+)'
    match = re.search(pattern, response)
    if match:
        score = int(match.group(1))
        return max(1, min(10, score))  # Clamp to 1-10
    
    return 5  # Default if not found


def verify_claims(response: str, client) -> List[str]:
    """
    Identify factual claims that need verification.
    
    Args:
        response: AI response to check
        client: OpenAI client
        
    Returns:
        List of claims that need verification
    """
    prompt = f"""Review this response and list any factual claims that should be verified:
    
    Response: {response}
    
    List each claim on a new line. If no claims need verification, respond with "None".
    
    Claims:"""
    
    try:
        verification = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        claims_text = verification.choices[0].message.content.strip()
        
        if "none" in claims_text.lower():
            return []
        
        claims = [c.strip() for c in claims_text.split('\n') if c.strip()]
        return claims
    except Exception:
        return []


class SafeAssistant:
    """Safe AI assistant with safeguards."""
    
    def __init__(self):
        """Initialize the safe assistant."""
        load_dotenv()
        
        if not OPENAI_AVAILABLE:
            raise ImportError("openai library not installed")
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        
        self.client = openai.OpenAI(api_key=api_key)
        
        self.system_message = """You are a helpful IoT assistant. 
        Always include a confidence score (1-10) in your responses like: "Confidence: 7"
        Be honest about uncertainty. If you're not sure, say so."""
    
    def answer(self, question: str) -> Dict:
        """
        Answer a question with appropriate safeguards.
        
        Args:
            question: User's question
            
        Returns:
            Dictionary with answer, confidence, and verification info
        """
        question_type = classify_question(question)
        
        if question_type == 'math':
            code, explanation = handle_math_question(question, self.client)
            return {
                "answer": f"Math problem detected. Generated code:\n\n```python\n{code}\n```\n\n{explanation}",
                "confidence": 7,  # Code generation is generally reliable
                "needs_verification": [],
                "question_type": "math",
                "code": code
            }
        
        # For general and realtime questions, use AI
        try:
            messages = [
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": question}
            ]
            
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            
            answer = response.choices[0].message.content
            confidence = get_confidence_score(answer)
            
            # Check for claims needing verification
            needs_verification = verify_claims(answer, self.client)
            
            # Add warning for realtime questions
            if question_type == 'realtime':
                answer = "⚠️  Note: AI may not have current information. Verify with reliable sources.\n\n" + answer
            
            return {
                "answer": answer,
                "confidence": confidence,
                "needs_verification": needs_verification,
                "question_type": question_type
            }
        except Exception as e:
            return {
                "answer": f"Error: {str(e)}",
                "confidence": 0,
                "needs_verification": [],
                "question_type": question_type
            }


def main():
    """Main function to run the safe assistant."""
    print("🛡️  Safe IoT Assistant")
    print("Type 'quit' to exit\n")
    
    try:
        assistant = SafeAssistant()
    except Exception as e:
        print(f"Error initializing assistant: {e}")
        return
    
    while True:
        try:
            question = input("Question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                break
            
            if not question:
                continue
            
            result = assistant.answer(question)
            
            print(f"\nAnswer ({result['question_type']}):")
            print(result['answer'])
            print(f"\nConfidence: {result['confidence']}/10")
            
            if result['needs_verification']:
                print("\n⚠️  Claims needing verification:")
                for claim in result['needs_verification']:
                    print(f"  - {claim}")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
