"""
File: polymorphism.py
Author: Somnath
Date: 24/05/26
Description: Polymorphism
"""


### Polymorphissm with Functions and MEthods
## base class
class Shape:
    def area(self):
        return "The area of the figure"


## Derived class 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


##DErived class 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


## Fucntion that demonstrates polymorphism

def print_area(shape):
    print(f"the area is {shape.area()}")


rectangle = Rectangle(4, 5)
circle = Circle(3)

print_area(rectangle)
print_area(circle)



