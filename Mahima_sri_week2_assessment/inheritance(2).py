class person():
    def __init__(self,name,qualification):
        self.name=name
        self.qualification=qualification
        
    def details(self):
        print(f"{self.name}:{self.qualification}")
        
class Employee(person):
    def __init__(self, name, id, department):
        self.name=name
        self.id= id
        self.department=department
        
    def details(self):
        print(f"{self.name},{self.id},{self.department}")
        
class Manager(person):
    def __init__(self, name, id, department):
        self.name=name
        self.id= id
        self.department=department
    def details(self):
        print(f"{self.name},{self.id},{self.department}")
    def approve_leave(self):
        print(f"Manager {self.name} has approved the leave")
        
manager =Manager("Alice", 101, "manager")
manager.details()
manager.approve_leave()