# Parent Class
class Product:
    def __init__(self, product_name, price):
        self.__product_name = product_name
        self.__price = price

    # Getters
    def get_product_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    # Setters
    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_price(self, price):
        self.__price = price

    # Calculate Price
    def calculatePrice(self):
        return self.__price

    # String Method
    def __str__(self):
        return (f"Product Name : {self.__product_name}\n"
                f"Price        : Rs.{self.__price}")


# Child Class
class DiscountProduct(Product):
    def __init__(self, product_name, price, discount_percentage):
        super().__init__(product_name, price)
        self.__discount_percentage = discount_percentage

    # Getter
    def get_discount_percentage(self):
        return self.__discount_percentage

    # Setter
    def set_discount_percentage(self, discount_percentage):
        self.__discount_percentage = discount_percentage

    # Overriding calculatePrice()
    def calculatePrice(self):
        discount = self.get_price() * self.__discount_percentage / 100
        return self.get_price() - discount

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nDiscount     : {self.__discount_percentage}%"
                f"\nFinal Price  : Rs.{self.calculatePrice()}")


# Driver Program
product = DiscountProduct("Laptop", 80000, 15)

print("Product Details")
print(product)

print("\nAfter Updating Discount")
product.set_discount_percentage(20)
print(product)

print("\nAfter Updating Price")
product.set_price(90000)
print(product)