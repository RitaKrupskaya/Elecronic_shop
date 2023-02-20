class Product:
    discount = 0.85

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def get_total_price(self):
        self.price = self.price * self.amount
        return self.price

    def apply_discount(self):
        self.price = self.price * self.discount
        return self.price


product1 = Product('Ноутбук', 20000, 2)
product2 = Product('Наушники', 5000, 15)

print(product1.get_total_price())
print(product2.get_total_price())

Product.discount = 0.6
product1.apply_discount()
print(product1.price)
print(product2.price)
