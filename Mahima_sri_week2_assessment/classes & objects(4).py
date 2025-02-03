class Student:
    def __init__(self, name, roll_number):
        self.name=name
        self.roll_number=roll_number
        
    def student_details(self):
        print(f"The name of the student is: {self.name}")
        print(f"The rool number of the student is:{self.roll_number}")
    
s=Student("mahima","22H55A0511")
s.student_details()

        