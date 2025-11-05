class ReplayAttack:
    def __init__(self, target_system):
        self.target_system = target_system

    def execute(self, captured_data):
        """
        Simulates a replay attack by sending previously captured data to the target system.
        
        :param captured_data: The data that was previously captured and is to be replayed.
        """
        print(f"Executing replay attack on {self.target_system} with captured data: {captured_data}")
        # Logic to send captured_data to the target_system would go here
        # This could involve simulating network packets or API calls
        # For example:
        # self.target_system.send_data(captured_data)
        return True

    def log_attack(self):
        """
        Logs the details of the replay attack for analysis.
        """
        print(f"Replay attack executed on {self.target_system}.")