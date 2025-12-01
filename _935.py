from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car: Starting engine... Vroom!")
        return "Car engine started"
    
    def stop_engine(self):
        print("Car: Stopping engine...")
        return "Car engine stopped"

class Bike(Vehicle):
    def start_engine(self):
        print("Bike: Starting engine... Brrrr!")
        return "Bike engine started"
    
    def stop_engine(self):
        print("Bike: Stopping engine...")
        return "Bike engine stopped"



car = Car()
car.start_engine()
car.stop_engine()
print()

bike = Bike()
bike.start_engine()
bike.stop_engine()
print()