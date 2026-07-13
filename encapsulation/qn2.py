class ShoppingCart:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__total_amount = 0


    def get_customer_name(self):
        return self.__customer_name

    def get_total_amount(self):
        return self.__total_amount


    def set_customer_name(self, name):
        self.__customer_name = name

 
    def add_item(self, price):
        if price > 0:
            self.__total_amount += price
            print("Item added.")
        else:
            print("Invalid price.")

    
    def remove_item(self, price):
        if price <= self.__total_amount:
            self.__total_amount -= price
            print("Item removed.")
        else:
            print("Cannot remove. Amount exceeds total.")


    def display_bill(self):
        print("\n----- Shopping Bill -----")
        print("Customer :", self.__customer_name)
        print("Total Amount :", self.__total_amount)



cart = ShoppingCart("Sanjay")

cart.add_item(500)
cart.add_item(700)
cart.display_bill()

cart.remove_item(300)
cart.display_bill()

cart.remove_item(2000)