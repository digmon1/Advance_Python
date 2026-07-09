class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"Area of rectangle: {self.length* self.breadth}")
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print(f"Perimeter of Rectangle: {p}")
l=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
R1=Rectangle(l,b)
R1.perimeter()