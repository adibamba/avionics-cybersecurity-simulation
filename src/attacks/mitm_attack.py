class MITMAttack:
    def __init__(self, target_ip, attacker_ip):
        self.target_ip = target_ip
        self.attacker_ip = attacker_ip

    def execute_attack(self):
        print(f"Executing MITM attack on {self.target_ip} from {self.attacker_ip}")
        # Logic to intercept and manipulate traffic goes here

    def stop_attack(self):
        print(f"Stopping MITM attack on {self.target_ip}")
        # Logic to stop the attack goes here

    def log_attack(self):
        print(f"Logging MITM attack on {self.target_ip} from {self.attacker_ip}")
        # Logic to log the attack details goes here