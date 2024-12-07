class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
class Library:
    def __init__(self):
        self.list = []
        
    def add_book(self,book):
        newlist =[
            f"Title:{book.title}",
            f"Author:{book.author}",
            f"Price:{book.price}",
        ]
        self.list.append(newlist)
    
    def show_book(self):
        for i in self.list:
            print(f"\n{i}\n")

book1 = Book("Great Man","F. Ane Fit","$10.99")
book2 = Book("The story about APT","Fake Man","$12.50")
book3 = Book(1984,"George Orwell","$9.75")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Books in library:")
print(library.show_book())
