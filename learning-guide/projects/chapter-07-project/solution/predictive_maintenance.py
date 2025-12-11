"""
Predictive Maintenance System - Complete Solution
Chapter 7 Project

Demonstrates Gemini's multimodal capabilities.
"""

import os
from dotenv import load_dotenv

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class PredictiveMaintenanceSystem:
    """Predictive maintenance system using Gemini."""
    
    def __init__(self):
        """Initialize system."""
        load_dotenv()
        
        if not GEMINI_AVAILABLE:
            raise ImportError("google-generativeai library not installed")
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def analyze_sensor_data(self, data: str) -> str:
        """Analyze sensor data."""
        try:
            prompt = f"Analyze this sensor data for anomalies and predict maintenance needs:\n\n{data}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """Main function."""
    print("🔧 Predictive Maintenance System")
    print("Type 'quit' to exit\n")
    
    try:
        system = PredictiveMaintenanceSystem()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            data = input("Sensor data (or 'quit'): ").strip()
            if data.lower() == 'quit':
                break
            result = system.analyze_sensor_data(data)
            print(f"\nAnalysis: {result}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
