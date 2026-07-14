# Parent Class
class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    # Getters
    def get_account_number(self):
        return self.__account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def get_balance(self):
        return self.__balance

    # Setters
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_account_holder_name(self, account_holder_name):
        self.__account_holder_name = account_holder_name

    def set_balance(self, balance):
        self.__balance = balance

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}")
        else:
            print("Invalid deposit amount.")

    # Withdraw Method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn Rs.{amount}")
        else:
            print("Insufficient Balance.")

    # String Method
    def __str__(self):
        return (f"Account Number : {self.__account_number}\n"
                f"Account Holder : {self.__account_holder_name}\n"
                f"Balance        : Rs.{self.__balance}")


# Child Class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.__interest_rate = interest_rate

    # Getter
    def get_interest_rate(self):
        return self.__interest_rate

    # Setter
    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    # Calculate Interest
    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate / 100
        return interest

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nInterest Rate : {self.__interest_rate}%"
                f"\nInterest      : Rs.{self.calculate_interest()}")


# Driver Program
account = SavingsAccount("1001", "Sanjay", 50000, 5)

print("Initial Details")
print(account)

print("\nAfter Deposit")
account.deposit(10000)
print(account)

print("\nAfter Withdrawal")
account.withdraw(15000)
print(account)