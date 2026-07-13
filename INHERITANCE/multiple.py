class parent1:
    def earn(self):
        print("Parent 1 Earning")

    def money(self):
        print("Parent 1 money")

class parent2(parent1):
    def play(self):
        print("Parent 2 Earning")

    def money(self):
        print("Parent 2 money")

class Child(parent2):
    def cry(self):
        print("Child crying")

c = Child()
c.money()
c.earn()
c.play()
c.cry()