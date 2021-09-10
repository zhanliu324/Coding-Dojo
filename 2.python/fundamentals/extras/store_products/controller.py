from store import Store
from product import Product

store1 = Store("Store One")
apple = Product("apple", "abc123", 1.00, "fruit")
bread = Product("bread", "aac211", 2.00, "bakery")

apple.print_info()
# store1.add_prodcut(apple).add_prodcut(bread).sell_product("abc123")
# print([product.name for product in store1.products])
store1.add_prodcut(apple).add_prodcut(bread).inflation(0.1).set_clearance("fruit", 0.3)
for product in store1.products:
    product.print_info()