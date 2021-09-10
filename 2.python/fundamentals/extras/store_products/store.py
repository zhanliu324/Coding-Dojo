class Store:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []

    def add_prodcut(self, new_product):
        self.products.append(new_product)
        return self
        
    def sell_product(self, id):
        for product in self.products:
            if product.id == id:
                print(f"{product.name} is sold.")
                self.products.pop(self.products.index(product))
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
            # print(f"price of {product.name}: ${product.price}.")
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
                # print(f"price of {product.name}: ${product.price}.")
        return self