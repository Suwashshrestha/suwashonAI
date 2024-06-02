
import math
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
# Create an object of the class
rectangle = Rectangle(7, 10)
print("Area of rectangle is:", rectangle.area())
circle = Circle(7)
print("Area of circle is:", circle.area())
