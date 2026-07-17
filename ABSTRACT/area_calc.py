from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        print(f"Area of Rectangle = {area}")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Area of Circle = {area:.2f}")


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        print(f"Area of Triangle = {area}")


rectangle = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(8, 6)

rectangle.area()
circle.area()
triangle.area()