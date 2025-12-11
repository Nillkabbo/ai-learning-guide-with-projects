"""Tests for Chapter 29 Future Architecture."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from future_architecture import FutureArchitecture
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_edge_processing():
    """Test edge processing."""
    architecture = FutureArchitecture()
    result = architecture.edge_process({"sensor": "temp_01"})
    assert result["edge"] is True


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_privacy_preserving():
    """Test privacy-preserving processing."""
    architecture = FutureArchitecture()
    sensitive_data = {"user_id": "user_123", "temperature": 25.5}
    result = architecture.privacy_preserving_process(sensitive_data)
    assert result["privacy_preserved"] is True
    assert "user_id" not in result.get("safe_data", {})


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
