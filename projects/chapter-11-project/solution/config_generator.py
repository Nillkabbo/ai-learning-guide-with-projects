"""
Validated IoT Configuration Generator - Complete Solution
Chapter 11 Project

Demonstrates structured output generation with JSON mode and Pydantic validation.
"""

import os
import json
from typing import Dict, Optional
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    from pydantic import BaseModel, Field, ValidationError
    PYDANTIC_AVAILABLE = True
except ImportError:
    PYDANTIC_AVAILABLE = False


class DeviceConfig(BaseModel):
    """Pydantic model for device configuration validation."""
    device_id: str = Field(..., description="Unique device identifier")
    device_type: str = Field(..., description="Type of IoT device")
    settings: Dict = Field(default_factory=dict, description="Device settings")
    enabled: bool = Field(default=True, description="Whether device is enabled")
    location: Optional[str] = Field(None, description="Device location")


def generate_json_config(requirements: str, client) -> Dict:
    """Generate JSON configuration using structured prompting."""
    prompt = f"""Generate a JSON configuration for an IoT device based on these requirements:
{requirements}

Return a JSON object with the following structure:
{{
    "device_id": "unique identifier",
    "device_type": "sensor type",
    "settings": {{"key": "value"}},
    "enabled": true,
    "location": "optional location"
}}"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}  # JSON mode
        )
        config_json = response.choices[0].message.content
        return json.loads(config_json)
    except Exception as e:
        raise ValueError(f"Failed to generate config: {str(e)}")


def validate_config(config: Dict) -> tuple[bool, Optional[str]]:
    """Validate configuration using Pydantic."""
    if not PYDANTIC_AVAILABLE:
        return True, None  # Skip validation if Pydantic not available
    
    try:
        DeviceConfig(**config)
        return True, None
    except ValidationError as e:
        return False, str(e)


def generate_config(requirements: str, client, max_retries: int = 3) -> Dict:
    """Generate and validate device configuration."""
    for attempt in range(max_retries):
        try:
            # Generate JSON config
            config = generate_json_config(requirements, client)
            
            # Validate with Pydantic
            is_valid, error = validate_config(config)
            if is_valid:
                return config
            else:
                print(f"Validation failed (attempt {attempt + 1}): {error}")
                if attempt < max_retries - 1:
                    # Retry with validation feedback
                    requirements += f"\n\nPrevious attempt failed validation: {error}"
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"Generation failed (attempt {attempt + 1}): {str(e)}")
    
    raise ValueError("Failed to generate valid configuration after retries")


def main():
    """Main function."""
    print("⚙️  IoT Configuration Generator")
    print("Type 'quit' to exit\n")
    
    load_dotenv()
    
    if not OPENAI_AVAILABLE:
        print("Error: openai library not installed")
        return
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment")
        return
    
    client = openai.OpenAI(api_key=api_key)
    
    while True:
        try:
            requirements = input("Configuration requirements (or 'quit'): ").strip()
            if requirements.lower() == 'quit':
                break
            
            if not requirements:
                continue
            
            config = generate_config(requirements, client)
            print(f"\nGenerated Config:\n{json.dumps(config, indent=2)}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
