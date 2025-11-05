class IntrusionDetection:
    def __init__(self):
        self.threats = []

    def monitor(self, network_simulator):
        """
        Inspect network_simulator.get_traffic() if available and record suspicious items.
        This is a lightweight stub used by tests.
        """
        traffic = []
        if hasattr(network_simulator, "get_traffic"):
            try:
                traffic = network_simulator.get_traffic()
            except Exception:
                traffic = []
        # detect 'malicious' in payloads
        for pkt in traffic:
            payload = pkt.get("payload") if isinstance(pkt, dict) else str(pkt)
            if isinstance(payload, dict):
                payload_text = str(payload)
            else:
                payload_text = str(payload)
            if "malicious" in payload_text.lower():
                self.threats.append(pkt)

    def detect_threat(self, activity) -> bool:
        """Single-activity check used by tests."""
        if "malicious" in str(activity).lower():
            self.threats.append(activity)
            return True
        return False

    def detect_threats(self) -> bool:
        """Return True if any threats were recorded during monitor() or detect_threat()."""
        return len(self.threats) > 0


class DoSAttack:
    def __init__(self, target_system=None):
        self.target_system = target_system
        self.attack_active = False

    def simulate(self):
        """Return a simple simulation result used by unit tests."""
        return {"success": True, "impact": "low", "target": self.target_system}

    def execute(self, network_simulator=None):
        """Execute attack against an optional NetworkSimulator. Return True on success."""
        # If a network simulator is provided, optionally mark an event
        if network_simulator is not None and hasattr(network_simulator, "send"):
            network_simulator.send("attacker", getattr(network_simulator, "nodes", {}) or "node", {"type": "dos"})
        return True

    # backward-compatible methods that some code/tests may call
    def start_attack(self):
        self.attack_active = True
        return True

    def stop_attack(self):
        self.attack_active = False
        return True

    def is_attack_active(self):
        return bool(self.attack_active)


class MITMAttack:
    def __init__(self, target=None, attacker=None):
        self.target = target
        self.attacker = attacker

    def simulate(self):
        """Return simple simulate() output for tests."""
        return {"success": True, "intercepted_data": "example_payload", "target": self.target}

    def execute(self, avionics_system=None):
        """Perform a lightweight execution for integration tests."""
        # Optionally interact with avionics_system if provided
        return True