def test_login_invalid(auth):
    response = auth.login("wrong", "wrong")
    assert response.status_code == 400
    assert "message" in response.json()


def test_login_success(auth):
    response = auth.login("emilys", "emilyspass")
    assert response.status_code == 200, f"Получили {response.status_code}"
    assert isinstance(response.json()["accessToken"], str)
    assert len(response.json()["accessToken"]) > 0


def test_get_me_success(auth, token):
    response = auth.get_me(token)
    assert response.status_code == 200
    assert response.json()["username"] == "emilys"


def test_get_me_without_token(auth):
    response = auth.get_me("")
    assert response.status_code == 401
    assert "message" in response.json()


def test_refresh_success(auth):
    login_response = auth.login("emilys", "emilyspass")
    refresh_token = login_response.json()["refreshToken"]
    refresh_response = auth.refresh(refresh_token)
    assert login_response.status_code == 200, f"Login failed: {login_response.status_code}"

    data = refresh_response.json()
    assert "accessToken" in data, "Нет accessToken в ответе"
    assert isinstance(data["accessToken"], str)
    assert len(data["accessToken"]) > 0
