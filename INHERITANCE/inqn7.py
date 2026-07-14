# Parent Class
class Vehicle:
    def __init__(self, registration_number, brand):
        self.__registration_number = registration_number
        self.__brand = brand

    # Getters
    def get_registration_number(self):
        return self.__registration_number

    def get_brand(self):
        return self.__brand

    # Setters
    def set_registration_number(self, registration_number):
        self.__registration_number = registration_number

    def set_brand(self, brand):
        self.__brand = brand

    # String Method
    def __str__(self):
        return (f"Registration Number : {self.__registration_number}\n"
                f"Brand               : {self.__brand}")


# Child Class
class Car(Vehicle):
    def __init__(self, registration_number, brand, model, price):
        super().__init__(registration_number, brand)
        self.__model = model
        self.__price = price

    # Getters
    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    # Setters
    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nModel               : {self.__model}"
                f"\nPrice               : Rs.{self.__price}")


# Grandchild Class
class ElectricCar(Car):
    def __init__(self, registration_number, brand, model, price,
                 battery_capacity, charging_time):
        super().__init__(registration_number, brand, model, price)
        self.__battery_capacity = battery_capacity
        self.__charging_time = charging_time

    # Getters
    def get_battery_capacity(self):
        return self.__battery_capacity

    def get_charging_time(self):
        return self.__charging_time

    # Setters
    def set_battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity

    def set_charging_time(self, charging_time):
        self.__charging_time = charging_time

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nBattery Capacity    : {self.__battery_capacity} kWh"
                f"\nCharging Time       : {self.__charging_time} Hours")


# Driver Program
car = ElectricCar(
    "BA-01-1234",
    "Tesla",
    "Model 3",
    6500000,
    75,
    8
)

print("Electric Car Details")
print(car)

print("\nAfter Updating Details")

car.set_price(7000000)
car.set_battery_capacity(80)
car.set_charging_time(7)

print(car)