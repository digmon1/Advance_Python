class Human:
    def __init__(self,name,size,color):
        self.name=name
        self.size=size
        self.color=color
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

h1=Human("Sanjay Kumar Shrestha",5.8,"Grain")
h2=Human("Virat Kholi",5,"Complexion")

h1.display()
print()
h2.display()