"""
File: singleInheritance.py
Author: Somnath
Date: 24/05/26
Description: Single inheritance
"""


class Car():
    def __init__(self, owner, windows, doors, engineType):
        self.owner = owner
        self.windows = windows
        self.doors = doors
        self.engineType = engineType

    def car_feature(self):
        print(f"{self.owner} will be driving {self.engineType} car")

class Tesla(Car):
    def __init__(self, owner, windows, doors, engineType, is_selfdrive):
        super().__init__(owner, windows, doors, engineType)
        self.is_selfdrive = is_selfdrive

    def feature(self):
        print(f"{self.owner} will drive {self.engineType} car and this car is having self drive feature {self.is_selfdrive}")

Tesla1 = Tesla('Krish', 4, 5, 'Electric', True)
print(Tesla1)
print(Tesla1.owner)
print(Tesla1.windows)
Tesla1.car_feature()
Tesla1.feature()
