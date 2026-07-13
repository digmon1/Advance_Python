class ATM:
    def __init__(self, customer_name, pin, balance):
        self.__customer_name = customer_name
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin

    def check_balance(self, entered_pin):
        if self.verify_pin(entered_pin):
            print("Current Balance:", self.__balance)
        else:
            print("Incorrect PIN.")

    def deposit(self, entered_pin, amount):
        if self.verify_pin(entered_pin):
            if amount > 0:
                self.__balance += amount
                print("Deposit Successful.")
            else:
                print("Invalid Amount.")
        else:
            print("Incorrect PIN.")

    def withdraw(self, entered_pin, amount):
        if self.verify_pin(entered_pin):
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal Successful.")
            else:
                print("Insufficient Balance.")
        else:
            print("Incorrect PIN.")

    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.__pin = new_pin
            print("PIN Changed Successfully.")
        else:
            print("Incorrect Old PIN.")

    def display_info(self, entered_pin):
        if self.verify_pin(entered_pin):
            print("Customer Name:", self.__customer_name)
            print("Balance:", self.__balance)
        else:
            print("Incorrect PIN.")


class Bank:
    def __init__(self):
        self.customers = []

    def create_account(self):
        acc = input("Enter Account Number: ")
        name = input("Enter Customer Name: ")
        pin = input("Set PIN: ")
        balance = float(input("Enter Initial Balance: "))

        customer = ATM(name, pin, balance)
        self.customers.append([acc, customer])

        print("Account Created Successfully.")

    def search_account(self, acc):
        for customer in self.customers:
            if customer[0] == acc:
                return customer[1]
        return None

    def deposit(self):
        acc = input("Enter Account Number: ")
        account = self.search_account(acc)

        if account:
            pin = input("Enter PIN: ")
            amount = float(input("Enter Amount: "))
            account.deposit(pin, amount)
        else:
            print("Account Not Found.")

    def withdraw(self):
        acc = input("Enter Account Number: ")
        account = self.search_account(acc)

        if account:
            pin = input("Enter PIN: ")
            amount = float(input("Enter Amount: "))
            account.withdraw(pin, amount)
        else:
            print("Account Not Found.")

    def check_balance(self):
        acc = input("Enter Account Number: ")
        account = self.search_account(acc)

        if account:
            pin = input("Enter PIN: ")
            account.check_balance(pin)
        else:
            print("Account Not Found.")

    def display_all(self):
        print("\n----- All Customers -----")

        for customer in self.customers:
            print("Account Number:", customer[0])


bank = Bank()

while True:
    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display All Customers")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit()

    elif choice == "3":
        bank.withdraw()

    elif choice == "4":
        bank.check_balance()

    elif choice == "5":
        bank.display_all()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")