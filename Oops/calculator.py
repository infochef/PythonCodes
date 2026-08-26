"""
File: calculator.py
Author: Somnath
Date: 24/08/26
Description: Class for Basic Arithmetic Operations
"""


class Calculator:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self):
        add = self.value1 + self.value2
        return f"Summation of the given inputs is: {add}"

    def subtract(self):
        subtract = self.value1 - self.value2
        return f"Difference of the given inputs is: {subtract}"

    def product(self):
        product = self.value1 * self.value2
        return f"Product of the given inputs is: {product}"

    def division(self):
        devide = self.value1 / self.value2
        return f"Devision of the given inputs is: {devide}"

    def floordivision(self):
        floordivision = self.value1 // self.value2
        return f"Floordivision of the given inputs is: {floordivision}"

    def mod(self):
        mod = self.value1 % self.value2
        return f"Mod of the given inputs is: {mod}"

    def run_all(self):
        return (
            self.add(),
            self.subtract(),
            self.product(),
            self.division(),
            self.floordivision(),
            self.mod()
        )

calculator1 = Calculator(5, 6)
calculator2 = Calculator(2, 3)
calculator3 = Calculator(3, 7)
calculator4 = Calculator(9, 12)

print(calculator1.run_all())
print(calculator2.run_all())
print(calculator3.run_all())
print(calculator4.run_all())