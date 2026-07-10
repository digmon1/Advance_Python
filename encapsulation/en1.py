class Bank:
    bank_name='LbeBank'
    def __init__(self, name,account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance
    def display(self):
        print(f'Bank Name: {self.bank_name}')
        print("Bank Account Details")
        print("Account Holder:", self.__name)
        print("Account Number:", self.__account_number)
        print("Balance:", self.__balance)
        print("--"*50)
        
        def getName(self):
            return self.__name
        
        def setName(self, name):
            self.__name = name

        def getAccount(self,acc):
            return self.__account_number
        
        def setAccount(self, acc):
            self.__account_number = acc
        
        def getBalance(self):
            return self.__balance
        
        def setBalance(self, amount):
            self.__balance = amount
        
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

i = 1
customers = []
while True:
    print()
    name=input(f'Enter Customer Name: ')
    acc=int(input(f'Enter Customer {i} account number: '))
    balance=float(input(f'Enter Customer {i} initial balance: '))
    c=Bank(name, acc, balance)
    customers.append(c)
    i += 1
    
    option=input('Do you want to add another customer? (y/n): ')
    if option.lower()=='no':
        break
    else:
        continue

for customer in customers:
    customer.display()
    