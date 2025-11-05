import unittest
from src.simulation.avionics_system import AvionicsSystem
from src.simulation.network_simulator import NetworkSimulator
from src.simulation.flight_controller import FlightController
from src.defense.intrusion_detection import IntrusionDetection
from src.attacks.dos_attack import DoSAttack
from src.attacks.mitm_attack import MITMAttack

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.avionics_system = AvionicsSystem()
        self.network_simulator = NetworkSimulator()
        self.flight_controller = FlightController(self.avionics_system)
        self.intrusion_detection = IntrusionDetection()
        self.dos_attack = DoSAttack()
        self.mitm_attack = MITMAttack()

    def test_avionics_system_initialization(self):
        self.assertIsNotNone(self.avionics_system)

    def test_network_simulator_initialization(self):
        self.assertIsNotNone(self.network_simulator)

    def test_flight_controller_initialization(self):
        self.assertIsNotNone(self.flight_controller)

    def test_dos_attack(self):
        result = self.dos_attack.execute(self.network_simulator)
        self.assertTrue(result)

    def test_mitm_attack(self):
        result = self.mitm_attack.execute(self.avionics_system)
        self.assertTrue(result)

    def test_intrusion_detection(self):
        # 1. Add malicious traffic to the simulator first
        self.network_simulator.send("attacker_ip", "victim_ip", "malicious_payload")
        
        # 2. Now, run the monitor method
        self.intrusion_detection.monitor(self.network_simulator)
        
        # 3. The assertion should now pass because a threat was found
        self.assertTrue(self.intrusion_detection.detect_threats())

if __name__ == '__main__':
    unittest.main()