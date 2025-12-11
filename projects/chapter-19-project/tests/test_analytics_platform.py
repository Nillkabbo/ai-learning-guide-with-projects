"""Tests for Chapter 19 Analytics Platform."""
import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from analytics_platform import app
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_ingest_event():
    """Test event ingestion."""
    client = TestClient(app)
    response = client.post("/events", json={
        "event_type": "device_status",
        "data": {"device_id": "device_01", "status": "online"}
    })
    assert response.status_code == 200
    assert "status" in response.json()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
