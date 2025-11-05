from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key: bytes = None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        """Accept str or bytes, return token as str."""
        if isinstance(data, str):
            data = data.encode("utf-8")
        token = self.cipher.encrypt(data)
        return token.decode("utf-8")

    def decrypt(self, token):
        """Accept token as str or bytes, return plaintext as str."""
        if isinstance(token, str):
            token = token.encode("utf-8")
        data = self.cipher.decrypt(token)
        return data.decode("utf-8")

    def get_key(self) -> bytes:
        return self.key

    def set_key(self, key: bytes):
        self.cipher = Fernet(key)
        self.key = key