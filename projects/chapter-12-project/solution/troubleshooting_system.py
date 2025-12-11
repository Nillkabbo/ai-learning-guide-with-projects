"""
Domain-Specific IoT Troubleshooting System - Complete Solution
Chapter 12 Project

Demonstrates domain-specific prompting with expert personas and domain knowledge.
"""

import os
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


DOMAIN_KNOWLEDGE = """IoT Domain Knowledge:
- Protocols: MQTT, CoAP, HTTP, WebSocket
- Communication: WiFi, Bluetooth, LoRaWAN, Zigbee
- Sensors: Temperature, Humidity, Pressure, Motion, Light
- Common Issues: Calibration drift, connectivity loss, power issues, firmware bugs
- Standards: IEEE 802.15.4, LoRaWAN 1.0, MQTT 3.1.1
- Best Practices: Regular calibration, secure communication, power management"""


def create_expert_persona() -> str:
    """Create domain expert persona prompt."""
    return """You are a senior IoT systems engineer with 15+ years of experience in:
- Industrial IoT deployments
- Sensor calibration and maintenance
- Network protocols (MQTT, CoAP, LoRaWAN)
- Device troubleshooting and diagnostics
- Industry standards and best practices

You diagnose issues using deep technical knowledge, industry terminology, and proven troubleshooting methodologies.
Always provide actionable, technically accurate solutions."""


def diagnose_issue(device_status: str, client) -> str:
    """Diagnose device issue using domain expertise."""
    system_prompt = f"""{create_expert_persona()}

{DOMAIN_KNOWLEDGE}

Analyze the device issue and provide a domain-specific diagnosis with:
1. Root cause analysis using IoT domain knowledge
2. Technical solution with industry-standard approaches
3. Actionable steps using proper IoT terminology"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Diagnose this IoT device issue: {device_status}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function."""
    print("🔧 Domain-Specific IoT Troubleshooting")
    print("Type 'quit' to exit\n")
    
    load_dotenv()
    
    if not OPENAI_AVAILABLE:
        print("Error: openai library not installed")
        return
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found")
        return
    
    client = openai.OpenAI(api_key=api_key)
    
    while True:
        try:
            status = input("Device status (or 'quit'): ").strip()
            if status.lower() == 'quit':
                break
            
            if not status:
                continue
            
            diagnosis = diagnose_issue(status, client)
            print(f"\nDiagnosis:\n{diagnosis}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
