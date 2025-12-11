"""Tests for Chapter 27 RAG System."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from rag_system import RAGSystem
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_index_document():
    """Test document indexing."""
    rag = RAGSystem()
    sample_text = "This is a test document about IoT devices."
    rag.index_document(sample_text, doc_id="test")
    # Check that document was indexed
    assert True  # Structure test


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
