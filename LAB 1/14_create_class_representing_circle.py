#create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    radius = int(input("Enter the radius of the circle: "))

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c = Circle()
print("Area of the circle is:", c.area())

print("Perimeter of the circle is:", c.perimeter())