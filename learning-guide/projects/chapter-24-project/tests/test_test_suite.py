"""Tests for Chapter 24 Test Suite."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from test_suite import validate_command, TestUnitTests
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_validate_command():
    """Test command validation."""
    result = validate_command("device_01:restart")
    assert result["valid"] is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
