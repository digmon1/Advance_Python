class Inventory:
    def __init__(self, pid, name, quantity, price):
        self.pid = pid
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_stock(self, qty):
        self.quantity += qty

    def remove_stock(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
        else:
            print("Not enough stock")

    def total_value(self):
        return self.quantity * self.price

    def low_stock(self):
        if self.quantity < 10:
            return "Low Stock"
        else:
            return "Stock Available"

    def display(self):
        print("\nProduct ID:", self.pid)
        print("Product Name:", self.name)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Inventory Value:", self.total_value())
        print("Status:", self.low_stock())


inventory = [
    Inventory(1, "Mouse", 15, 800),
    Inventory(2, "Keyboard", 8, 1500),
    Inventory(3, "Monitor", 5, 18000)
]

inventory[0].add_stock(5)
inventory[1].remove_stock(3)

print("Inventory Report")

for item in inventory:
    item.display()