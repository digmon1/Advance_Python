class ATM:
    def __init__(self, customer_name, pin, balance):
        self.__customer_name = customer_name
        self.__pin = pin
        self.__balance = balance


    def get_balance(self):
        return self.__balance


    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin


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


    def check_balance(self, entered_pin):
        if self.verify_pin(entered_pin):
            print("Current Balance:", self.__balance)
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
            print("\n----- Account Details -----")
            print("Customer Name :", self.__customer_name)
            print("Balance :", self.__balance)
        else:
            print("Incorrect PIN.")



atm = ATM("Sanjay", "1234", 10000)

atm.check_balance("1234")

atm.deposit("1234", 3000)

atm.withdraw("1234", 5000)

atm.check_balance("1234")

atm.change_pin("1234", "5678")

atm.display_info("5678")