class Animal:
    def speak(self):
        print(f"The animal sounds")
        
class cat(Animal):
    def speak(self):
        print(f"the cat meows")
        
class dog(Animal):
    def speak(self):
        print(f"The dog barks")
        
d=dog()
d.speak()
 
c=cat()
c.speak()