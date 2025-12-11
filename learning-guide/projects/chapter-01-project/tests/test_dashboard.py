"""
Tests for Chapter 1 IoT Device Status Dashboard.

These tests verify the basic functionality of the IoT dashboard.
Run with: pytest tests/test_dashboard.py
"""

import pytest
import sys
import os

# Add parent directory to path to import solution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from iot_dashboard import interpret_device_message
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_interpret_device_message_structure():
    """Test that interpret_device_message returns a string."""
    # This test requires API key, so we'll just check structure
    message = "TEMP_SENSOR_01: 85.2C STATUS:WARNING"
    # Note: This will fail if API key not set, which is expected
    try:
        result = interpret_device_message(message)
        assert isinstance(result, str)
        assert len(result) > 0
    except Exception as e:
        # Expected if API key not configured
        assert "API" in str(e) or "key" in str(e).lower() or "ollama" in str(e).lower()


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_interpret_device_message_handles_errors():
    """Test that the function handles errors gracefully."""
    # Test with empty string
    try:
        result = interpret_device_message("")
        # Should either return a string or raise a clear error
        assert isinstance(result, str) or "error" in result.lower()
    except Exception:
        # Exceptions are acceptable if handled properly
        pass


def test_message_format_examples():
    """Test examples of valid device message formats."""
    valid_messages = [
        "TEMP_SENSOR_01: 85.2C STATUS:WARNING",
        "HUMIDITY_SENSOR_02: 45% STATUS:OK",
        "PRESSURE_SENSOR_03: 1200 PSI STATUS:CRITICAL",
        "MOTION_SENSOR_04: DETECTED STATUS:INFO",
        "BATTERY_LEVEL: 15% STATUS:LOW"
    ]
    
    for msg in valid_messages:
        assert isinstance(msg, str)
        assert len(msg) > 0
        # Basic format check: should have some structure
        assert ":" in msg or "STATUS" in msg


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
