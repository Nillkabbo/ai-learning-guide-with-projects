"""
Tests for Chapter 4 Safe Assistant.

Run with: pytest tests/test_safe_assistant.py
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from safe_assistant import classify_question, get_confidence_score
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_classify_math_question():
    """Test classification of math questions."""
    assert classify_question("What is 2 + 2?") == "math"
    assert classify_question("Calculate 10 * 5") == "math"
    assert classify_question("Solve 100 / 4") == "math"


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_classify_realtime_question():
    """Test classification of real-time questions."""
    assert classify_question("What is the current time?") == "realtime"
    assert classify_question("What's the latest news?") == "realtime"
    assert classify_question("What happened today?") == "realtime"


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_classify_general_question():
    """Test classification of general questions."""
    assert classify_question("What is IoT?") == "general"
    assert classify_question("Explain sensors") == "general"


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_get_confidence_score():
    """Test confidence score extraction."""
    assert get_confidence_score("Answer. Confidence: 8") == 8
    assert get_confidence_score("Confidence: 10") == 10
    assert get_confidence_score("confidence: 3") == 3
    assert get_confidence_score("No confidence mentioned") == 5  # Default


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
