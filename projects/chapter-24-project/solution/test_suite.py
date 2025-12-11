"""
IoT Command Validation Test Suite - Complete Solution
Chapter 24 Project

Demonstrates comprehensive testing: unit, integration, regression, load tests.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import os
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

load_dotenv()


def validate_command(command: str) -> dict:
    """Validate IoT command."""
    if not command or ":" not in command:
        return {"valid": False, "error": "Invalid format"}
    
    parts = command.split(":")
    if len(parts) != 2:
        return {"valid": False, "error": "Invalid format"}
    
    device_id, action = parts
    valid_actions = ["restart", "stop", "start", "status"]
    
    if action not in valid_actions:
        return {"valid": False, "error": f"Invalid action: {action}"}
    
    return {"valid": True, "device_id": device_id, "action": action}


# Unit Tests
class TestUnitTests:
    """Unit tests with mocks."""
    
    def test_validate_command_valid(self):
        """Test valid command."""
        result = validate_command("device_01:restart")
        assert result["valid"] is True
        assert result["device_id"] == "device_01"
        assert result["action"] == "restart"
    
    def test_validate_command_invalid_format(self):
        """Test invalid format."""
        result = validate_command("invalid")
        assert result["valid"] is False
        assert "error" in result
    
    def test_validate_command_invalid_action(self):
        """Test invalid action."""
        result = validate_command("device_01:invalid_action")
        assert result["valid"] is False


# Integration Tests
@pytest.mark.skipif(not OPENAI_AVAILABLE, reason="OpenAI not available")
class TestIntegrationTests:
    """Integration tests with real API."""
    
    def test_ai_validation_integration(self):
        """Test AI validation with real API."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            pytest.skip("API key not available")
        
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Validate: device_01:restart"}]
        )
        assert response.choices[0].message.content is not None


# AI Regression Tests
class TestAIRegression:
    """AI regression tests."""
    
    # Golden dataset
    GOLDEN_DATASET = [
        ("device_01:restart", True),
        ("device_02:status", True),
        ("invalid", False),
    ]
    
    def test_golden_dataset(self):
        """Test against golden dataset."""
        for command, expected_valid in self.GOLDEN_DATASET:
            result = validate_command(command)
            assert result["valid"] == expected_valid, f"Failed for: {command}"


# Load Tests
class TestLoadTests:
    """Load tests."""
    
    def test_multiple_validations(self):
        """Test multiple validations."""
        commands = [f"device_{i}:restart" for i in range(100)]
        results = [validate_command(cmd) for cmd in commands]
        assert all(r["valid"] for r in results)
        assert len(results) == 100


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
