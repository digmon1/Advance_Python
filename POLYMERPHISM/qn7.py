class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance


acc1 = BankAccount("Sanjay", 5000)
acc2 = BankAccount("Ram", 7000)

print("Combined Balance =", acc1 + acc2)