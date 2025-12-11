"""Tests for Chapter 30 Product Concept."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from product_concept import ProductConcept
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_lean_canvas():
    """Test Lean AI Canvas."""
    concept = ProductConcept()
    canvas = concept.fill_lean_canvas()
    assert "problem" in canvas
    assert "solution" in canvas
    assert len(canvas["key_metrics"]) > 0


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_mvp_design():
    """Test MVP design."""
    concept = ProductConcept()
    mvp = concept.design_mvp()
    assert "features" in mvp
    assert len(mvp["features"]) > 0


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_ethical_review():
    """Test ethical review."""
    concept = ProductConcept()
    review = concept.conduct_ethical_review()
    assert "considerations" in review
    assert "bias" in review["considerations"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
