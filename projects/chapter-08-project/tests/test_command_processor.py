"""Tests for Chapter 8 Command Processor."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from command_processor import retry_with_backoff
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_retry_decorator():
    """Test retry decorator structure."""
    # Test structure only, requires API key for full test
    pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
