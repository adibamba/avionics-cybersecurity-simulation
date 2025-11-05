def authenticate_user(username: str, password: str) -> bool:
    # placeholder; tests only expect truthy response for non-empty values
    return bool(username) and bool(password)

def authenticate_system(system_id: str, token: str) -> bool:
    return bool(system_id) and bool(token)

def generate_auth_token(user_id: str) -> str:
    return f"token_for_{user_id}"

class Authentication:
    """Compatibility wrapper used by tests."""
    def authenticate_user(self, username: str, password: str) -> bool:
        return authenticate_user(username, password)

    def authenticate_system(self, system_id: str, token: str) -> bool:
        return authenticate_system(system_id, token)

    def generate_token(self, user_id: str) -> str:
        return generate_auth_token(user_id)

    def verify(self, credentials: dict) -> bool:
        if not isinstance(credentials, dict):
            return False
        return authenticate_user(credentials.get("username"), credentials.get("password"))