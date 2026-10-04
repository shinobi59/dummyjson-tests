import pytest
from api.auth import AuthApi
from api.carts import CartsApi
from api.client import ApiClient
from api.products import ProductsApi

BASE_URL = "https://dummyjson.com"

@pytest.fixture(scope="session")
def api():
    client = ApiClient(base_url=BASE_URL)
    yield client
    client.close()

@pytest.fixture(scope="session")
def auth(api):
    return AuthApi(api)

@pytest.fixture(scope="session")
def token(auth):
    response = auth.login("emilys", "emilyspass")
    assert response.status_code == 200, f"Login failed: {response.status_code}"
    return response.json()["accessToken"]

@pytest.fixture(scope="session")
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture(scope="session")
def products(api):
    return ProductsApi(api)

@pytest.fixture
def product_data():
    return {
        "title": "Test Product",
        "description": "Test description",
        "price": 99,
        "category": "test",
        "brand": "TestBrand",
    }

@pytest.fixture(scope="session")
def carts(api):
    return CartsApi(api)

@pytest.fixture
def cart_data():
    return {
      "userId": 1,
      "products": [
        {"id": 144, "quantity": 4},
        {"id": 98, "quantity": 1}
      ]
    }
