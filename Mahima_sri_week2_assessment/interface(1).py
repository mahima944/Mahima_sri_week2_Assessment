import math
from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle(IShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth  
    
    def calculate_area(self):
        return self.length * self.breadth  
    
class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * (self.radius ** 2) 


r = Rectangle(2, 3)
print(f"The area of the rectangle is: {r.calculate_area()}")

c = Circle(3)
print(f"The area of the circle is: {c.calculate_area()}")
