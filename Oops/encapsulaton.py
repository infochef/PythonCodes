"""
File: encapsulaton.py
Author: Somnath
Date: 24/05/26
Description: Encapsulation
"""

# Encapsulation using Getter and Setter method
class Person:
    def __init__(self, name, age):
        self.__name = name # double underscore shows that the variable is private variable
        self.__age = age # double underscore shows that the variable is private variable
        # self.height = height  # public variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cant be in negative")

person = Person('Krish', 34)

print(person.get_name())
print(person.get_age())

person.set_age(35)
print(person.get_age())

person.set_age(-1)