"""
File: multipleInheritance.py
Author: Somnath
Date: 24/05/26
Description: 
"""

class Animal():
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

    def characterstics(self):
        return print(f"{self.name} is a herbivores animal")

class Pet:
    def __init__(self, ownerName, **kwargs):
        super().__init__(**kwargs)
        self.ownerName = ownerName

    def get_ownerName(self):
        return print(f"{self.ownerName} is having {self.name} animal.")

class Dog(Animal, Pet):
    def __init__(self, name, ownerName, nature):
        super().__init__(name=name, ownerName=ownerName)
        self.nature = nature

    def get_dog_feature(self):
        return print(f"{self.ownerName} is having {self.name} and the nature of the {self.name} is {self.nature}")

dog1 = Dog('Dog', 'Sam', 'Friendly')
dog1.characterstics()
dog1.get_ownerName()
dog1.get_dog_feature()
