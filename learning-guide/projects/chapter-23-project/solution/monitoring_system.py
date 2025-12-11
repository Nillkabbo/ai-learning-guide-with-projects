"""
IoT Monitoring Dashboard - Complete Solution
Chapter 23 Project

Demonstrates observability: structured logging, metrics, distributed tracing.
"""

import os
import logging
import json
from typing import Dict, List
from datetime import datetime
from collections import defaultdict
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MonitoringSystem:
    """IoT monitoring system with observability."""
    
    def __init__(self):
        """Initialize monitoring system."""
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or not OPENAI_AVAILABLE:
            raise ValueError("OpenAI API key required")
        
        self.client = openai.OpenAI(api_key=api_key)
        self.metrics = defaultdict(list)
        self.traces = []
        self.trace_counter = 0
    
    def log_interaction(self, level: str, message: str, context: Dict):
        """Log interaction with structured logging."""
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message,
            **context
        }
        
        # Structured JSON log
        logger.info(json.dumps(log_data))
    
    def track_metric(self, name: str, value: float, tags: Dict = None):
        """Track a metric."""
        metric_entry = {
            "timestamp": datetime.now().isoformat(),
            "value": value,
            "tags": tags or {}
        }
        self.metrics[name].append(metric_entry)
    
    def start_trace(self, operation: str) -> str:
        """Start a distributed trace."""
        self.trace_counter += 1
        trace_id = f"trace_{self.trace_counter}"
        
        trace = {
            "trace_id": trace_id,
            "operation": operation,
            "start_time": datetime.now().isoformat(),
            "spans": []
        }
        self.traces.append(trace)
        
        return trace_id
    
    def end_trace(self, trace_id: str, status: str = "success"):
        """End a trace."""
        for trace in self.traces:
            if trace["trace_id"] == trace_id:
                trace["end_time"] = datetime.now().isoformat()
                trace["status"] = status
                trace["duration_ms"] = (
                    datetime.fromisoformat(trace["end_time"]) -
                    datetime.fromisoformat(trace["start_time"])
                ).total_seconds() * 1000
                break
    
    def process_with_monitoring(self, prompt: str) -> str:
        """Process request with full monitoring."""
        trace_id = self.start_trace("ai_request")
        
        try:
            self.log_interaction("info", "Processing request", {"prompt_length": len(prompt)})
            
            start_time = datetime.now()
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            end_time = datetime.now()
            
            duration = (end_time - start_time).total_seconds()
            result = response.choices[0].message.content
            
            # Track metrics
            if response.usage:
                self.track_metric("tokens_used", response.usage.total_tokens)
                self.track_metric("cost", (response.usage.total_tokens / 1_000_000) * 0.15)
            self.track_metric("latency_ms", duration * 1000)
            
            self.log_interaction("info", "Request completed", {
                "tokens": response.usage.total_tokens if response.usage else 0,
                "duration_ms": duration * 1000
            })
            
            self.end_trace(trace_id, "success")
            return result
            
        except Exception as e:
            self.log_interaction("error", "Request failed", {"error": str(e)})
            self.end_trace(trace_id, "error")
            return f"Error: {str(e)}"
    
    def get_dashboard_data(self) -> Dict:
        """Get dashboard data."""
        return {
            "metrics": {k: len(v) for k, v in self.metrics.items()},
            "traces": len(self.traces),
            "recent_traces": self.traces[-5:] if self.traces else []
        }


def main():
    """Main function."""
    print("📊 IoT Monitoring Dashboard")
    print("Type 'quit' to exit\n")
    
    try:
        monitor = MonitoringSystem()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            prompt = input("Query (or 'quit'): ").strip()
            if prompt.lower() == 'quit':
                break
            
            if not prompt:
                continue
            
            response = monitor.process_with_monitoring(prompt)
            print(f"\nResponse: {response}\n")
            
            # Show dashboard
            dashboard = monitor.get_dashboard_data()
            print(f"Metrics tracked: {dashboard['metrics']}")
            print(f"Total traces: {dashboard['traces']}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
