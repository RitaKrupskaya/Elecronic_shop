from main import Product


def test_product_atrb():
    product1 = Product('Computer', 25000, 3)
    assert product1.name == 'Computer'
    assert product1.price == 25000
    assert product1.amount == 3
    assert product1.get_total_price() == 75000


def test_discount():
    product2 = Product('Airpods', 16000, 10)
    assert product2.apply_discount() == 12800