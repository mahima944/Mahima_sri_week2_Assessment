class Electronics:
    def __init__(self, name , price):
        self.name=name
        self.price=price
        
    def display(self):
        print (f"Brand: {self.name}\n price: {self.price}")
class MobileDevice(Electronics):
    def __init__(self, name, price,batterry_life):
        super().__init__(name, price)
        self.battery_life= batterry_life
        
    def display(self):
        super().display()
        print(f"battery : {self.battery_life}")
        
class Smartphone(MobileDevice):
    def __init__(self, name, price, battery_life, camera_quality):
        super().__init__(name, price, battery_life)
        self.camera_quality= camera_quality
        
    def display(self):
        super().display()
        print(f"camera:{self.camera_quality}")
        
s= Smartphone("Apple", 99999,128,150)
s.display()
        
        
        
        
    