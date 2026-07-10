class Bank:
    bank_name='LbeBank'
    def __init__(self, name,account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def display(self):
        print(f'Bank Name: {self.bank_name}')
        print("Bank Account Details")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("--"*50)
    
    def deposit(self, acc, amount):
        if self.account_number == acc:
            self.balance = self.balance + amount
            print(f'{amount} is deposited successfully')
        else:
            print("Invalid account number!! please enter the valid account number")
    
    def withdraw(self, acc, amount):
        if self.account_number == acc:
            if self.balance >= amount:
                self.balance = self.balance - amount
                print(f'{amount} is withdrawn successfully')
            else:
                print("Insufficient balance")
        else:
            print("Invalid account number!! please enter the valid account number")

pappu=Bank('Pappu Gupta', 12345, 5000)
subodh=Bank('Subodh Acharya', 54321,0)
pappu.display()
subodh.display()
subodh.deposit(54321,22)
subodh.display()