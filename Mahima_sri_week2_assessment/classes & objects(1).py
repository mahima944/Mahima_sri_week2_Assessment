class Employee:
    def __init__(self,name, id, department):
        self.name=name
        self.id=id
        self.department=department
        
e=Employee("mahi",1, "cse")
print(f"name:{e.name}, id:{e.id}, department:{e.department}")
        
    