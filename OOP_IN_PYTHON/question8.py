class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def display(self):
        print(self.pid, self.name, self.price)


products = [
    Product(1, "Mouse", 800),
    Product(2, "Keyboard", 1500),
    Product(3, "Monitor", 18000),
    Product(4, "Speaker", 3500),
    Product(5, "Laptop", 75000)
]

print("All Products")
for p in products:
    p.display()

expensive = max(products, key=lambda x: x.price)
cheap = min(products, key=lambda x: x.price)

average = sum(p.price for p in products) / len(products)

print("\nMost Expensive Product")
expensive.display()

print("\nCheapest Product")
cheap.display()

print("\nAverage Price =", average)