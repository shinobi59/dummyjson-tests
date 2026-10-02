from api.client import ApiClient

class AuthApi:
    def __init__(self, client: ApiClient):
        self.client = client

    def login(self, username, password):
        payload = {
            'username': username,
            'password': password,
            'expiresInMins': 30
        }
        response = self.client.post('/auth/login', json=payload)
        return response

    def get_me(self, token):
        response = self.client.get(f'/auth/me', headers={'Authorization': f'Bearer {token}'})
        return response

    def refresh(self, refresh_token):
        payload = {
            'refreshToken': refresh_token,
            'expiresInMins': 30
        }
        response = self.client.post('/auth/refresh', json=payload)
        return response


