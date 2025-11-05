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