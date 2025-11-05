import unittest
from src.attacks.dos_attack import DoSAttack
from src.attacks.mitm_attack import MITMAttack
from src.attacks.injection_attack import InjectionAttack
from src.attacks.replay_attack import ReplayAttack

class TestAttacks(unittest.TestCase):

    def setUp(self):
        self.dos_attack = DoSAttack()
        self.mitm_attack = MITMAttack()
        self.injection_attack = InjectionAttack()
        self.replay_attack = ReplayAttack()

    def test_dos_attack(self):
        result = self.dos_attack.simulate()
        self.assertTrue(result['success'])
        self.assertIn('impact', result)

    def test_mitm_attack(self):
        result = self.mitm_attack.simulate()
        self.assertTrue(result['success'])
        self.assertIn('intercepted_data', result)

    def test_injection_attack(self):
        result = self.injection_attack.simulate()
        self.assertTrue(result['success'])
        self.assertIn('injected_payload', result)

    def test_replay_attack(self):
        result = self.replay_attack.simulate()
        self.assertTrue(result['success'])
        self.assertIn('replayed_data', result)

if __name__ == '__main__':
    unittest.main()