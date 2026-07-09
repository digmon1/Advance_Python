class Human:
    college= "LBEF" #class Vaiable
    def __init__(self): # a, b,c (local variable)
        self.name="LBEF"
        self.size=27        # name,size,color (instance variable)
        self.color='White'
    def display(self):
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"color: {self.color}")
    def eat(self):
        print("Human is eating....")
    def sleep(self):
        print("Human is sleeping....")
    def walk(self):
        print("Human is walking....")

h1=Human()       #h1,h2 (refrence variable)
h2=Human()

h1.display()
print()
h2.display()