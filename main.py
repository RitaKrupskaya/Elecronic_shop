class Product:
    discount = 0.8
    storage_of_products = []

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        Product.storage_of_products.append(self)

    def get_total_price(self):
        self.price = self.price * self.amount
        return self.price

    def apply_discount(self):
        self.price = self.price * self.discount
        return self.price


