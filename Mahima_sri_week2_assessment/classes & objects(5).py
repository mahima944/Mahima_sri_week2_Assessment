class product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def check_availability(self,quantity):

        if quantity<= self.stock :
            print(f"{quantity}  {self.name} are available")
        else:
            print(f"{quantity} request product {self.name} are not available")
    
    
p=product("laptop",500, 100)
print(p.check_availability(90))
        

            
        