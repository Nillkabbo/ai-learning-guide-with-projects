"""Tests for Chapter 15 Production Agent."""
import pytest
import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from production_agent import ProductionAgent
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_state_persistence():
    """Test state save/load."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        state_file = f.name
    
    try:
        agent = ProductionAgent(state_file=state_file)
        agent.state["test"] = "value"
        agent.save_state()
        
        # Create new agent instance to test loading
        agent2 = ProductionAgent(state_file=state_file)
        assert agent2.state.get("test") == "value"
    finally:
        if os.path.exists(state_file):
            os.remove(state_file)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
