class Parent:
    def __init__(self, name, age, salary   ):
        self.pname= name
        self.age = age
        self.salary =salary
    
    def displayP(self):
        print(f'Parent Name: {self.pname}')
        print(f'Parent Age: {self.age}')
        print(f'Parent Salary: {self.salary}')
        print("--"*50)

class child(Parent):
    def __init__(self, name, id, fees, pname, age , salary):
        self.cname =name
        self.id = id
        self.fees = fees
    
    def displayC(self):
        print(f'Child Name: {self.cname}')
        print(f'Child id: {self.age}')
        print(f'Child fees : {self.fees}')
        print("--"*50)
        print()

c= child("Pcps college, 23,2555555")
c.displayP()

