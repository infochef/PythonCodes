"""
File: polymorphism_abstract.py
Author: Somnath
Date: 24/05/26
Description: Polymorphism with Abstract Base Classes
Abstract Base Classes (ABCs) are used to define common methods for a group of related objects. They
can enforce that derived classes implement particular methods, promoting consistency across different
implementations.
"""

from abc import ABC, abstractmethod


## Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


## Derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car enginer started"


## Derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle enginer started"


# Function that demonstrates polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())


## create objects of cAr and Motorcycle

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)


