"""Tests for Chapter 14 Tool Agent."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from tool_agent import control_device, get_device_status
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_control_device():
    """Test device control function."""
    result = control_device("device_01", "restart")
    assert "device_01" in result
    assert "restart" in result


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_get_device_status():
    """Test get device status function."""
    result = get_device_status("device_01")
    assert "device_01" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
