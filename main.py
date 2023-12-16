class Product:
    def __init__(self, product_name, price, quantity):
        self.name = product_name
        self.price = price
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price



    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity has to be not zero!")
        self._quantity = value

    @price.setter
    def price(self, condition):
        if condition  < 0:
            raise ValueError("Price has to be not less zero")
        else:
            self._price = condition


pr1 = Product("Apple", 10_000, 12)
print(pr1.name, pr1.price, pr1.quantity)