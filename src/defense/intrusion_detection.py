class IntrusionDetection:
    def __init__(self):
        self.threats = []

    def detect_intrusion(self, network_traffic):
        # Analyze network traffic for suspicious patterns
        for packet in network_traffic:
            if self.is_suspicious(packet):
                self.threats.append(packet)
                self.alert_admin(packet)

    def is_suspicious(self, packet):
        # Implement logic to determine if a packet is suspicious
        # This is a placeholder for actual detection logic
        return "malicious" in packet

    def alert_admin(self, packet):
        # Notify the administrator of the detected intrusion
        print(f"Intrusion detected: {packet}")