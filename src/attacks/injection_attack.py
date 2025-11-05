class InjectionAttack:
    def __init__(self, target_system):
        self.target_system = target_system

    def execute(self, payload):
        print(f"Executing injection attack on {self.target_system} with payload: {payload}")
        # Simulate the injection attack logic here
        # For example, modify the state of the target system or inject malicious commands
        success = self._inject_payload(payload)
        return success

    def _inject_payload(self, payload):
        # Logic to inject the payload into the target system
        # This is a placeholder for actual injection logic
        print(f"Payload '{payload}' injected successfully.")
        return True

    def report(self):
        # Generate a report of the attack
        return f"Injection attack executed on {self.target_system}."