"""Tests for Chapter 12 Troubleshooting System."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from troubleshooting_system import create_expert_persona
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_expert_persona():
    """Test expert persona creation."""
    persona = create_expert_persona()
    assert "IoT" in persona or "engineer" in persona
    assert len(persona) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
