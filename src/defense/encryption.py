from cryptography.fernet import Fernet

class Encryption:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data: bytes) -> bytes:
        return self.cipher.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        return self.cipher.decrypt(token)

    def get_key(self) -> bytes:
        return self.key

    def set_key(self, key: bytes):
        self.cipher = Fernet(key)