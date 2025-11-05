class NetworkSimulator:
    def __init__(self, network_topology):
        self.network_topology = network_topology
        self.nodes = self.initialize_network()

    def initialize_network(self):
        nodes = {}
        for node in self.network_topology:
            nodes[node] = {"status": "active", "data": []}
        return nodes

    def simulate_traffic(self, source, destination, data):
        if source in self.nodes and destination in self.nodes:
            self.nodes[source]["data"].append(data)
            print(f"Simulating traffic from {source} to {destination}: {data}")
        else:
            print("Invalid source or destination")

    def introduce_latency(self, node, latency):
        if node in self.nodes:
            print(f"Introducing {latency}ms latency to {node}")
            # Simulate latency logic here
        else:
            print("Invalid node")

    def simulate_failure(self, node):
        if node in self.nodes:
            self.nodes[node]["status"] = "failed"
            print(f"Simulating failure for node: {node}")
        else:
            print("Invalid node")

    def reset_node(self, node):
        if node in self.nodes:
            self.nodes[node]["status"] = "active"
            self.nodes[node]["data"] = []
            print(f"Resetting node: {node}")
        else:
            print("Invalid node")