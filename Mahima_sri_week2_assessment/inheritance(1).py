class Vehicle:
    def get_vehicle(self):
        print("this is vehicle class")
        
class car(Vehicle):
    def get_car(self):
        print("this is car class")
        
class Bike(Vehicle):
    def get_bike(self):
        print("this is bike class")
        
class ElectricCar(car):
    def get_electriccar(self):
        print("this is electric car class")
        
e= ElectricCar()
e.get_electriccar()
e.get_car()
e.get_vehicle()
b= Bike()
b.get_bike()
b.get_vehicle()
