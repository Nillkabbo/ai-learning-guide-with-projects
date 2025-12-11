"""Tests for Chapter 25 DevOps System."""
import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from devops_system import app
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_health_check():
    """Test health check."""
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_deploy():
    """Test deployment."""
    client = TestClient(app)
    response = client.post("/deploy", json={"version": "v1.0.1"})
    assert response.status_code == 200
    assert "status" in response.json()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
