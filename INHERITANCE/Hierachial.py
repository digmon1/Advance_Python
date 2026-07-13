class parent:
    def earn(self):
        print("Parent Earning")

class Child1(parent):
    def play(self):
        print('Child playing')

class Child2(parent):
    def cry (self):
        print("GrandChild crying")

c=Child1()
c.earn()
c.play()
#c.cry()
    