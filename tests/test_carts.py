import allure

@allure.feature("Carts")
@allure.title("Получение всех корзин")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_carts(carts):
    response = carts.get_all()
    assert response.status_code == 200
    assert "carts" in response.json()
    assert isinstance(response.json()["carts"], list)
    assert len(response.json()["carts"]) > 0, "Список корзин пуст"

@allure.feature("Carts")
@allure.title("Получение корзины по id")
@allure.severity(allure.severity_level.NORMAL)
def test_get_cart_by_id(carts):
    response = carts.get_by_id(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "products" in response.json()
    assert isinstance(response.json()["products"], list)

@allure.feature("Carts")
@allure.title("Получение корзины по user")
@allure.severity(allure.severity_level.NORMAL)
def test_get_carts_by_user(carts):
    response = carts.get_by_user(1)
    assert response.status_code == 200
    for cart in response.json()["carts"]:
        assert cart["userId"] == 1

@allure.feature("Carts")
@allure.title("Получение неизвестной корзины")
@allure.severity(allure.severity_level.MINOR)
def test_get_unknown_cart(carts):
    response = carts.get_by_id(99999)
    assert response.status_code == 404
    assert "message" in response.json()

@allure.feature("Carts")
@allure.title("Создание корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_cart(carts, cart_data):
    add_cart = carts.create(cart_data)
    data = add_cart.json()
    assert add_cart.status_code == 201
    assert isinstance(data["id"], int)
    assert len(data["products"]) == len(cart_data["products"])

@allure.feature("Carts")
@allure.title("Расчёт total корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_cart_total_math(carts):
    response = carts.get_by_id(1)
    cart = response.json()

    expected = round(sum(product["total"] for product in cart["products"]), 2)
    actual = round(cart["total"], 2)

    assert actual == expected, \
        f"total корзины не совпадает: {actual} != {expected}"

@allure.feature("Carts")
@allure.title("Расчёт total продуктов")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_total_math(carts):
    response = carts.get_by_id(1)
    data = response.json()

    for product in data["products"]:
        expected = round(product["price"] * product["quantity"], 2)
        actual = round(product["total"], 2)
        assert actual == expected

@allure.feature("Carts")
@allure.title("Обновление корзины с merge")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_cart_with_merge(carts, cart_data):
    response = carts.update(1, cart_data, merge=True)
    assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"

    data = response.json()
    assert "products" in data, "Нет поля 'products' в ответе"
    # merge=True — в ответе должны быть и старые, и новые продукты
    assert len(data["products"]) >= len(cart_data["products"]), \
        f"merge не сработал: в ответе {len(data['products'])} продуктов"
