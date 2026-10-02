def test_get_all_products(products):
    response = products.get_all()
    assert response.status_code == 200

def test_get_products_pagination(products):
    page_1 = products.get_all(params={"limit": 5, "skip": 0})
    page_2 = products.get_all(params={"limit": 5, "skip": 5})
    assert page_1.status_code == 200
    assert page_2.status_code == 200
    assert len(page_1.json()["products"]) == 5
    assert len(page_2.json()["products"]) == 5
