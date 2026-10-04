import allure


def test_get_all_carts(carts):
    response = carts.get_all()
    assert response.status_code == 200
    assert "carts" in response.json()
    assert isinstance(response.json()["carts"], list)
    assert len(response.json()) > 0


def test_get_dart_by_id(carts):
    response = carts.get_by_id(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "products" in response.json()
    assert isinstance(response.json()["products"], list)


def test_get_carts_by_user(carts):
    response = carts.get_by_user(1)
    assert response.status_code == 200
    for carts in response.json()["carts"]:
        assert carts["userId"] == 1


def test_get_unknown_cart(carts):
    response = carts.get_by_id(99999)
    assert response.status_code == 404
    assert "message" in response.json()


def test_create_cart(carts, cart_data):
    add_cart = carts.create(cart_data)
    data = add_cart.json()
    assert add_cart.status_code == 201
    assert isinstance(data["id"], int)
    assert len(data["products"]) == len(cart_data["products"])


def test_cart_total_math(carts):
    response = carts.get_by_id(1)
    cart = response.json()
    expected = round(sum(product["quantity"] for product in cart["products"]), 2)
    actual = round(cart["total"], 2)
    assert actual == expected


def test_product_total_math(carts):
    response = carts.get_by_id(1)
    data = response.json()
    assert float(product["total"] == round(product["price"] * product["quantity"], 2))


def test_update_cart_with_merge(carts, cart_data):
    before = carts.get_by_id(1).json()
    before_count = len(before["products"])

    response = carts.update(1, cart_data, merge=True)
    assert response.status_code == 200

    after = carts.get_by_id(1).json()
    after_count = len(after["products"])

    assert after_count > before_count, \
        f"merge не сработал: было {before_count}, стало {after_count}"
