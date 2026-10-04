import allure

@allure.feature("Products")
@allure.title("Получить все продукты")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_products(products):
    response = products.get_all()
    assert response.status_code == 200

@allure.feature("Products")
@allure.title("Пагинация продукта")
@allure.severity(allure.severity_level.MINOR)
def test_get_products_pagination(products):
    page_1 = products.get_all(params={"limit": 5, "skip": 0})
    page_2 = products.get_all(params={"limit": 5, "skip": 5})
    assert page_1.status_code == 200
    assert page_2.status_code == 200
    assert len(page_1.json()["products"]) == 5
    assert len(page_2.json()["products"]) == 5

@allure.feature("Products")
@allure.title("Получить продукт по ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_product_by_id(products):
    response = products.get_by_id(1)
    data = response.json()
    assert data["id"] == 1
    assert response.status_code == 200
    assert data["title"] is not None

@allure.feature("Products")
@allure.title("Получить неизвестный продукт")
@allure.severity(allure.severity_level.MINOR)
def test_get_unknown_product(products):
    response = products.get_by_id(99999)
    data = response.json()
    assert response.status_code == 404

@allure.feature("Products")
@allure.title("Поиск продукта")
@allure.severity(allure.severity_level.NORMAL)
def test_search_products(products):
    response = products.search("phone")
    assert response.status_code == 200
    assert response.json()["products"] is not None
    for product in response.json()["products"]:
        assert product["title"] is not None

@allure.feature("Products")
@allure.title("Создать продукт")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_product(products, product_data):
    response = products.create(product_data)
    print(response.status_code)
    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["title"] == product_data["title"]

@allure.feature("Products")
@allure.title("Обновить продукт")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_product(products, product_data):
    updated_data = {**product_data, "title": "Updated title"}
    response = products.update(1, updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"
