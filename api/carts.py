from api.client import ApiClient


class CartsApi:
    def __init__(self, client: ApiClient):
        self.client = client

    def get_all(self, params=None):
        response = self.client.get('/carts', params=params)
        return response

    def get_by_id(self, cart_id):
        response = self.client.get(f'/carts/{cart_id}')
        return response

    def get_by_user(self, user_id):
        response = self.client.get(f'/carts/user/{user_id}')
        return response

    def create(self, cart_data):
        response = self.client.post('/carts/add', json=cart_data)
        return response

    def update(self, cart_id, cart_data, merge=True):
        params = {'merge': str(merge).lower()}
        response = self.client.put(f'/carts/{cart_id}', json=cart_data, params=params)
        return response

    def delete(self, cart_id):
        response = self.client.delete(f'/carts/{cart_id}')
        return response
