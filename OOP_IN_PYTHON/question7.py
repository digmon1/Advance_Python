class Car:
    def __init__(self, brand, model, price, fuel):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel = fuel

    def display(self):
        print("\nBrand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Fuel Type:", self.fuel)

    def affordable(self):
        if self.price < 3000000:
            print("Affordable")
        else:
            print("Not Affordable")

    def discount(self, percent):
        self.price = self.price - (self.price * percent / 100)


car = Car("Toyota", "Yaris", 3500000, "Petrol")

car.display()
car.affordable()

percent = float(input("Enter Discount Percentage: "))
car.discount(percent)

print("Price After Discount:", car.price)