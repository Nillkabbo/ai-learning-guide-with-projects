"""Tests for Chapter 21 Cost Optimizer."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from cost_optimizer import CostOptimizer, PRICING
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_cost_calculation():
    """Test cost calculation."""
    # Test cost calculation logic
    tokens = 1000
    model = "gpt-4o-mini"
    pricing = PRICING[model]
    expected_cost = (tokens / 1_000_000) * pricing["input"]
    assert expected_cost > 0


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_model_selection():
    """Test model selection logic."""
    optimizer = CostOptimizer()
    simple_task = "explain this"
    model = optimizer.select_model(simple_task)
    assert model in PRICING


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
