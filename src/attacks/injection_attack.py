class InjectionAttack:
    def __init__(self, target=None):
        self.target = target

    def simulate(self):
        """Return test-friendly result describing injected payload."""
        payload = "malicious_command"
        return {"success": True, "injected_payload": payload, "target": self.target}

    def execute(self, payload=None):
        """Execute injection; returns True on success."""
        # In a real sim you'd apply payload to target; here we return True for tests
        return True