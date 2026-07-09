class Rectangle:
    # Constructor
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Return type method for area
    def area(self):
        return self.length * self.breadth

    # Return type method for perimeter
    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Taking input from the user
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))

# Creating an object
R1 = Rectangle(l, b)

# Calling return type methods
print(f"Area of Rectangle: {R1.area()}")
print(f"Perimeter of Rectangle: {R1.perimeter()}")