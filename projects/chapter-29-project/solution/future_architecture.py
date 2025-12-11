"""
Next-Generation IoT Architecture - Complete Solution
Chapter 29 Project

Demonstrates future architecture: multimodal AI, edge concepts, privacy-preserving design.
"""

import os
from typing import Dict, Optional
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

load_dotenv()


class FutureArchitecture:
    """Next-generation IoT architecture."""
    
    def __init__(self):
        """Initialize future architecture."""
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key and OPENAI_AVAILABLE:
            self.client = openai.OpenAI(api_key=api_key)
        else:
            self.client = None
    
    def process_multimodal(self, text: str = None, image_path: str = None, sensor_data: Dict = None) -> str:
        """Process multimodal inputs."""
        if not self.client:
            return "AI client not available (demo mode)"
        
        messages = []
        
        # Add text
        if text:
            messages.append({"role": "user", "type": "text", "text": text})
        
        # Add image
        if image_path:
            try:
                import base64
                with open(image_path, "rb") as image_file:
                    image_data = base64.b64encode(image_file.read()).decode('utf-8')
                messages.append({
                    "role": "user",
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}
                })
            except Exception as e:
                return f"Error processing image: {e}"
        
        # Add sensor data as text
        if sensor_data:
            sensor_text = f"Sensor data: {sensor_data}"
            messages.append({"role": "user", "type": "text", "text": sensor_text})
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": messages}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def edge_process(self, data: Dict) -> Dict:
        """Process data at edge (simulated)."""
        # Simulate edge processing: fast, local, offline-capable
        return {
            "processed": True,
            "edge": True,
            "latency_ms": 10,  # Low latency
            "offline": True,
            "result": "Edge-processed data"
        }
    
    def privacy_preserving_process(self, data: Dict) -> Dict:
        """Process with privacy preservation."""
        # Simulate privacy-preserving processing
        # - Data minimization
        # - Local processing
        # - No external transmission of sensitive data
        processed = {
            "privacy_preserved": True,
            "data_minimized": True,
            "local_processing": True,
            "sensitive_fields_removed": ["user_id", "location"]
        }
        
        # Remove sensitive fields
        safe_data = {k: v for k, v in data.items() if k not in ["user_id", "location"]}
        processed["safe_data"] = safe_data
        
        return processed


def main():
    """Main function."""
    print("🚀 Next-Generation IoT Architecture")
    print("=" * 50)
    
    architecture = FutureArchitecture()
    
    # Demonstrate multimodal processing
    print("\n1. Multimodal Processing:")
    result = architecture.process_multimodal(
        text="Analyze this IoT device",
        sensor_data={"temperature": 25.5, "humidity": 60}
    )
    print(f"Result: {result[:100]}...")
    
    # Demonstrate edge processing
    print("\n2. Edge Processing:")
    edge_result = architecture.edge_process({"sensor": "temp_01", "value": 25.5})
    print(f"Edge result: {edge_result}")
    
    # Demonstrate privacy-preserving processing
    print("\n3. Privacy-Preserving Processing:")
    sensitive_data = {"user_id": "user_123", "location": "NYC", "temperature": 25.5}
    privacy_result = architecture.privacy_preserving_process(sensitive_data)
    print(f"Privacy result: {privacy_result}")
    
    print("\n" + "=" * 50)
    print("Future architecture concepts demonstrated!")


if __name__ == "__main__":
    main()
