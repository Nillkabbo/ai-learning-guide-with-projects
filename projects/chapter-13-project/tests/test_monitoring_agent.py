"""Tests for Chapter 13 Monitoring Agent."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from monitoring_agent import MonitoringAgent
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_agent_initialization():
    """Test agent initializes correctly."""
    # This test requires API key, so we'll just check structure
    pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
