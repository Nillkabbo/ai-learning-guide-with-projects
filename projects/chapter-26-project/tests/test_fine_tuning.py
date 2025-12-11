"""Tests for Chapter 26 Fine-Tuning."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from fine_tuning import prepare_training_data, save_training_file
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_prepare_training_data():
    """Test training data preparation."""
    examples = prepare_training_data()
    assert len(examples) > 0
    assert "messages" in examples[0]


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_save_training_file(tmp_path):
    """Test saving training file."""
    examples = prepare_training_data()
    filepath = tmp_path / "test.jsonl"
    save_training_file(examples, str(filepath))
    assert filepath.exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
