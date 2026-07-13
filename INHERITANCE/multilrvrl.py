class parent:
    def earn(self):
        print("Parent Earning")

class Child(parent):
    def play(self):
        print('Child playing')

class GrandChild(Child):
    def cry (self):
        print("GrandChild crying")

c=GrandChild()
c.earn()
c.play()
c.cry()
    