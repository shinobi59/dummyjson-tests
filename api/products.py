from api.client import ApiClient


class ProductsApi:
    def __init__(self, client: ApiClient):
        self.client = client

    def get_all(self, params=None):
        response = self.client.get('/products', params=params)
        return response

    def get_by_id(self, product_id):
        response = self.client.get(f'/products/{product_id}')
        return response

    def search(self, query, params=None):
        merged = {"q": query, **(params or {})}
        response = self.client.get('/products/search', params=merged)
        return response

    def get_by_category(self, category):
        response = self.client.get(f'/products/category/{category}')
        return response

    def create(self, product_data):
        response = self.client.post('/products/add', json=product_data)
        return response

    def update(self, product_id, product_data):
        response = self.client.put(f'/products/{product_id}', json=product_data)
        return response

    def partial_update(self, product_id, product_data):
        response = self.client.patch(f'/products/{product_id}', json=product_data)
        return response

    def delete(self, product_id):
        response = self.client.delete(f'/products/{product_id}')
        return response
