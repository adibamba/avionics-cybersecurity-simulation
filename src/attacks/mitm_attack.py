class MITMAttack:
    """
    Lightweight MITM attack stub. No self-imports or unittest code.
    """
    def __init__(self, target=None, attacker=None):
        self.target = target
        self.attacker = attacker
        self.intercepted = []

    def simulate(self):
        return {"success": True, "intercepted_data": "example_payload", "target": self.target}

    def execute(self, network_simulator=None):
        if network_simulator and hasattr(network_simulator, "send"):
            pkt = {"source": "nodeA", "dest": "nodeB", "payload": "intercepted"}
            self.intercepted.append(pkt)
            network_simulator.send("mitm", pkt["dest"], {"payload": "modified"})
        return True