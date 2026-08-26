"""
File: circle.py
Author: Somnath
Date: 24/08/26
Description: Circle Class for Area and Perimeter
"""


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        return f"For given {self.radius} area of circle is: {area}"

    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return f"For given {self.radius} perimeter of circle is: {perimeter}"

objcre = Circle(5)
area = objcre.calculate_area()
perimeter = objcre.calculate_perimeter()
print(area)
print(perimeter)
objcre.radius = 3
area = objcre.calculate_area()
perimeter = objcre.calculate_perimeter()
print(area)
print(perimeter)
