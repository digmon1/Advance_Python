class Payment:
    def pay(self, amount):
        print("Processing payment of Rs.", amount)


class CreditCard(Payment):
    def pay(self, amount):
        super().pay(amount)
        print("Paid using Credit Card")


class DebitCard(Payment):
    def pay(self, amount):
        super().pay(amount)
        print("Paid using Debit Card")


class UPI(Payment):
    def pay(self, amount):
        super().pay(amount)
        print("Paid using UPI")


class PayPal(Payment):
    def pay(self, amount):
        super().pay(amount)
        print("Paid using PayPal")


# Duck Typing Class
class Cash:
    def pay(self, amount):
        print("Paid Rs.", amount, "using Cash")


# Wallet with Operator Overloading
class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance


payments = [
    CreditCard(),
    DebitCard(),
    UPI(),
    PayPal(),
    Cash()
]

for payment in payments:
    payment.pay(2500)
    print()


wallet1 = Wallet("Sanjay", 3000)
wallet2 = Wallet("Ram", 5000)

print("Combined Wallet Balance =", wallet1 + wallet2)