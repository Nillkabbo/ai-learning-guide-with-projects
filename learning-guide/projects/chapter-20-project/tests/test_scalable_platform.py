"""Tests for Chapter 20 Scalable Platform."""
import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from scalable_platform import app
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_submit_task():
    """Test task submission."""
    client = TestClient(app)
    response = client.post("/tasks", json={"action": "monitor", "device": "device_01"})
    assert response.status_code == 200
    assert "task_id" in response.json()


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_health_check():
    """Test health check."""
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
