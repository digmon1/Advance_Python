class Human:
    college= "LBEF" #class Vaiable
    def __init__(self,a,b,c): # a, b,c (local variable)
        self.name=a
        self.size=b         # name,size,color (instance variable)
        self.color=c
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

    @classmethod
    def walk(cls):
        print("this is class method")

    @staticmethod
    def wish(stc):
        print("Good Morning!...")

h1=Human("Sanjay Kumar Shrestha",5.8,"Grain")       #h1,h2 (refrence variable)
h2=Human("Virat Kholi",5,"Complexion")

h1.display()
Human.walk()
print()
h2.display()
Human.walk()
