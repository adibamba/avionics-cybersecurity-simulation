class NetworkSimulator:
    def __init__(self, network_topology=None):
        """
        Lightweight, testable NetworkSimulator. Accepts optional topology.
        """
        self.topology = network_topology or {"nodes": []}
        # nodes stored as a dict for easy referencing in tests
        self.nodes = {n.get("id") if isinstance(n, dict) else n: {"status": "up"} for n in self.topology.get("nodes", [])}
        self.traffic = []

    def send(self, source, dest, payload):
        """Record a piece of simulated traffic."""
        self.traffic.append({"source": source, "dest": dest, "payload": payload})
        return True

    def get_traffic(self):
        return list(self.traffic)

    def add_node(self, node_id):
        self.nodes[node_id] = {"status": "up"}
        return True