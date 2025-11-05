class DoSAttack:
    def __init__(self, target_system):
        self.target_system = target_system
        self.attack_active = False

    def start_attack(self):
        self.attack_active = True
        print(f"Starting DoS attack on {self.target_system}")

    def stop_attack(self):
        self.attack_active = False
        print(f"Stopping DoS attack on {self.target_system}")

    def is_attack_active(self):
        return self.attack_active

    def simulate_attack(self):
        if self.attack_active:
            print(f"Simulating DoS attack on {self.target_system}...")
            # Here you would implement the logic to simulate the attack
            # For example, overwhelming the target with requests
        else:
            print("No active attack to simulate.")