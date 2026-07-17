from abc import ABC, abstractmethod

class FoodOrder(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def deliver(self):
        pass


class Pizza(FoodOrder):

    def prepare(self):
        print("Preparing Pizza...")

    def calculate_price(self):
        return 800

    def deliver(self):
        print("Pizza delivered successfully.")


class Burger(FoodOrder):

    def prepare(self):
        print("Preparing Burger...")

    def calculate_price(self):
        return 350

    def deliver(self):
        print("Burger delivered successfully.")


class Pasta(FoodOrder):

    def prepare(self):
        print("Preparing Pasta...")

    def calculate_price(self):
        return 500

    def deliver(self):
        print("Pasta delivered successfully.")


pizza = Pizza()
burger = Burger()
pasta = Pasta()

orders = [pizza, burger, pasta]

total_bill = 0

for order in orders:
    order.prepare()
    price = order.calculate_price()
    print("Price = Rs.", price)
    order.deliver()
    total_bill += price
    print()

print("Total Bill = Rs.", total_bill)