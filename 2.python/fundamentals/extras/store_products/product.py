class Product:
    def __init__(self, name, id, price, category) -> None:
        self.name = name
        self.id = id
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        print(f"Product name: {self.name}, category: {self.category}, price: {self.price}.")
        return self