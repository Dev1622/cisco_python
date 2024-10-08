from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car starts."

class Bike(Vehicle):
    def start(self):
        return "Bike starts."

#vehicle = Vehicle() abstract class cannot be instatiated
car = Car()
bike = Bike()
print(car.start())  # Output: Car starts.
print(bike.start())  # Output: Bike starts.