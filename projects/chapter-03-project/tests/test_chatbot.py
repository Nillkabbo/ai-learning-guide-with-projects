"""
Tests for Chapter 3 Enhanced Chatbot.

These tests verify the chatbot functionality and professional practices.
Run with: pytest tests/test_chatbot.py
"""

import pytest
import os
import sys
from unittest.mock import Mock, patch

# Add solution to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from chatbot import Chatbot
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_chatbot_initialization():
    """Test that chatbot initializes correctly."""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
        with patch('chatbot.openai.OpenAI'):
            chatbot = Chatbot()
            assert len(chatbot.conversation_history) == 1
            assert chatbot.conversation_history[0]["role"] == "system"
            assert chatbot.total_tokens == 0


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_chatbot_custom_system_message():
    """Test chatbot with custom system message."""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
        with patch('chatbot.openai.OpenAI'):
            custom_msg = "You are a Python expert."
            chatbot = Chatbot(system_message=custom_msg)
            assert chatbot.conversation_history[0]["content"] == custom_msg


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_clear_history():
    """Test that clear_history preserves system message."""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
        with patch('chatbot.openai.OpenAI'):
            chatbot = Chatbot()
            chatbot.conversation_history.append({"role": "user", "content": "test"})
            chatbot.conversation_history.append({"role": "assistant", "content": "response"})
            
            chatbot.clear_history()
            
            assert len(chatbot.conversation_history) == 1
            assert chatbot.conversation_history[0]["role"] == "system"


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_missing_api_key():
    """Test that missing API key raises appropriate error."""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="OPENAI_API_KEY"):
            Chatbot()


def test_project_structure():
    """Test that project has required files."""
    project_dir = os.path.join(os.path.dirname(__file__), '..')
    
    required_files = [
        'README.md',
        'requirements.txt',
        '.gitignore'
    ]
    
    for file in required_files:
        file_path = os.path.join(project_dir, file)
        assert os.path.exists(file_path), f"Missing required file: {file}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
