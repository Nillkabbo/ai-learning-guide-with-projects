"""
Tests for Chapter 5 Shopping Assistant.

Run with: pytest tests/test_shopping_assistant.py
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from shopping_assistant import search_products
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_search_products_by_category():
    """Test product search by category."""
    results = search_products(category="mouse")
    assert len(results) > 0
    assert all(p["category"] == "mouse" for p in results)


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_search_products_by_price():
    """Test product search by price."""
    results = search_products(max_price=50.0)
    assert len(results) > 0
    assert all(p["price"] <= 50.0 for p in results)


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_search_products_combined():
    """Test product search with both filters."""
    results = search_products(category="mouse", max_price=50.0)
    assert len(results) > 0
    assert all(p["category"] == "mouse" and p["price"] <= 50.0 for p in results)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
