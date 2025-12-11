"""Tests for Chapter 23 Monitoring System."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))

try:
    from monitoring_system import MonitoringSystem
    HAS_SOLUTION = True
except ImportError:
    HAS_SOLUTION = False
    pytestmark = pytest.mark.skip("Solution not available")


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_trace_management():
    """Test trace management."""
    monitor = MonitoringSystem()
    trace_id = monitor.start_trace("test_operation")
    assert trace_id.startswith("trace_")
    monitor.end_trace(trace_id)
    assert len(monitor.traces) > 0


@pytest.mark.skipif(not HAS_SOLUTION, reason="Solution not available")
def test_metric_tracking():
    """Test metric tracking."""
    monitor = MonitoringSystem()
    monitor.track_metric("test_metric", 42.0)
    assert "test_metric" in monitor.metrics


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
