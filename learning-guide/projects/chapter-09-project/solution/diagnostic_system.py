"""
Smart Diagnostic System - Complete Solution
Chapter 9 Project

Demonstrates prompt engineering patterns: zero-shot, few-shot, chain-of-thought, role-based.
"""

import os
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class DiagnosticSystem:
    """Smart diagnostic system using prompt engineering."""
    
    def __init__(self):
        """Initialize system."""
        load_dotenv()
        
        if not OPENAI_AVAILABLE:
            raise ImportError("openai library not installed")
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found")
        
        self.client = openai.OpenAI(api_key=api_key)
    
    def diagnose(self, device_status: str, method: str = "zero_shot") -> str:
        """Diagnose using specified method."""
        if method == "zero_shot":
            prompt = f"Diagnose this IoT device issue: {device_status}"
        elif method == "few_shot":
            prompt = f"""Here are examples:
Example 1: Device: TEMP_SENSOR, Status: WARNING, Reading: 95C
Diagnosis: Overheating. Check sensor calibration.

Now diagnose: {device_status}"""
        elif method == "chain_of_thought":
            prompt = f"""Diagnose this step by step:
1. Identify the issue
2. Determine possible causes
3. Recommend solution

Device status: {device_status}"""
        else:  # role_based
            prompt = f"""You are an expert IoT engineer. Diagnose this device issue:
{device_status}"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """Main function."""
    print("🔍 Smart Diagnostic System")
    print("Type 'quit' to exit\n")
    
    try:
        system = DiagnosticSystem()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            status = input("Device status (or 'quit'): ").strip()
            if status.lower() == 'quit':
                break
            method = input("Method (zero_shot/few_shot/chain_of_thought/role_based): ").strip() or "zero_shot"
            result = system.diagnose(status, method)
            print(f"\nDiagnosis: {result}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
