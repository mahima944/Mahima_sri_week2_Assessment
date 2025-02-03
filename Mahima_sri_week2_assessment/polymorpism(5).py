class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    
    def __add__(self, other):
        if isinstance(other, Book):
            return Book(f"{self.title} & {other.title}", self.author)
        

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Fantastic Beasts", "J.K. Rowling")

series = book1 + book2  

print(series)  
