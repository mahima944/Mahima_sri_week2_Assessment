class Book:
    def __init__(self,title, author,isued):
        self.title=title
        self.author=author
        self.isued=isued
        
    def display(self):
        print(f"The title of the book is:{self.title}")
        print(f"The author of book is: {self.author}")
        print(f"The isbn of the book is:{self.isued}")
        
b=Book("The Art of being Alone", "mahima", "22-12-2004")
b.display()