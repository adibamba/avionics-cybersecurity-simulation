import unittest
from src.defense.intrusion_detection import IntrusionDetection
from src.defense.encryption import Encryption
from src.defense.authentication import Authentication
from src.defense.firewall import Firewall

class TestDefenseMechanisms(unittest.TestCase):

    def setUp(self):
        self.intrusion_detection = IntrusionDetection()
        self.encryption = Encryption()
        self.authentication = Authentication()
        self.firewall = Firewall()

    def test_intrusion_detection(self):
        threat_detected = self.intrusion_detection.detect_threat("malicious_activity")
        self.assertTrue(threat_detected)

    def test_encryption(self):
        original_message = "Sensitive Data"
        encrypted_message = self.encryption.encrypt(original_message)
        decrypted_message = self.encryption.decrypt(encrypted_message)
        self.assertEqual(original_message, decrypted_message)

    def test_authentication(self):
        user_credentials = {"username": "test_user", "password": "secure_password"}
        is_authenticated = self.authentication.verify(user_credentials)
        self.assertTrue(is_authenticated)

    def test_firewall(self):
        access_granted = self.firewall.check_access("192.168.1.1")
        self.assertTrue(access_granted)

if __name__ == '__main__':
    unittest.main()