"""Tests for Chapter 11 Config Generator."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from config_generator import DeviceConfig, validate_config
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_device_config_validation():
    """Test Pydantic model validation."""
    valid_config = {
        "device_id": "sensor_01",
        "device_type": "temperature",
        "settings": {"threshold": 25.0},
        "enabled": True
    }
    is_valid, error = validate_config(valid_config)
    assert is_valid


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_device_config_invalid():
    """Test validation catches invalid config."""
    invalid_config = {
        "device_id": "sensor_01"
        # Missing required fields
    }
    is_valid, error = validate_config(invalid_config)
    assert not is_valid


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
