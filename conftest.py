import pytest
from api.auth import AuthApi
from api.client import ApiClient

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


