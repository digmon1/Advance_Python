class BankAccount:
    def __init__(self, acc_no, holder, balance):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Current Balance:", self.balance)


acc = BankAccount("1001", "Sanjay", 5000)

acc.deposit(2000)
acc.withdraw(3000)
acc.withdraw(6000)

acc.display_balance()