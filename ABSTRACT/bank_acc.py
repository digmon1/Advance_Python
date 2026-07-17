from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SavingsAccount(BankAccount):

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance.")

    def check_balance(self):
        print(f"Current Balance = Rs.{self.balance}")


class CurrentAccount(BankAccount):

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance.")

    def check_balance(self):
        print(f"Current Balance = Rs.{self.balance}")


saving = SavingsAccount(10000)
current = CurrentAccount(5000)

print("Savings Account")
saving.deposit(2000)
saving.withdraw(3000)
saving.check_balance()

print("\nCurrent Account")
current.deposit(1000)
current.withdraw(7000)
current.check_balance()