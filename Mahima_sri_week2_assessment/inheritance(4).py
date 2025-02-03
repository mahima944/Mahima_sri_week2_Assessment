class car():
    def move(self):
        print(f"car can move forward and backward")
        
class Airplane():
    def move(self):
        print(f"moves on the sky")
        
class FlyingCar(car,Airplane):
    def move(self):
        print(f"moves on ground and sky")
        
f=FlyingCar()
f.move()

a=Airplane()
a.move()

c=car()
c.move()