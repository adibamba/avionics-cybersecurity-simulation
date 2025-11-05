import time

class Metrics:
    """
    A simple class to collect and store simulation metrics.
    
    This acts as a central point for recording events like attacks,
    packets sent, or defense actions.
    """
    def __init__(self):
        # A dictionary to hold all our metrics.
        # We can store simple counters, lists of timings, etc.
        self._data = {
            "events": [],
            "counters": {},
            "start_time": time.time()
        }

    def increment(self, metric_name: str, count: int = 1):
        """
        Increments a named counter. If the counter doesn't exist, it's created.
        
        Example: metrics.increment("packets_sent")
        """
        current_count = self._data["counters"].get(metric_name, 0)
        self._data["counters"][metric_name] = current_count + count

    def record_event(self, event_name: str, details: dict = None):
        """
        Records a timestamped event.
        
        Example: metrics.record_event("dos_attack_started", {"target": "node1"})
        """
        event = {
            "timestamp": time.time(),
            "event": event_name,
            "details": details or {}
        }
        self._data["events"].append(event)

    def get_metrics(self) -> dict:
        """
        Returns a snapshot of all collected metrics.
        """
        # Add the total runtime to the output
        self._data["runtime_seconds"] = time.time() - self._data["start_time"]
        return self._data

    def print_summary(self):
        """
        Prints a simple summary of the collected metrics to the console.
        """
        summary = self.get_metrics()
        print("\n--- Simulation Metrics Summary ---")
        print(f"Total Runtime: {summary['runtime_seconds']:.2f} seconds")
        
        print("\nCounters:")
        if summary["counters"]:
            for name, value in summary["counters"].items():
                print(f"  - {name}: {value}")
        else:
            print("  (No counters recorded)")
            
        print(f"\nTotal Events Recorded: {len(summary['events'])}")
        print("--------------------------------\n")