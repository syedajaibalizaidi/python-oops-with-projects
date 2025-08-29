### Aggregation ->> Represents a realtionship where one object (the whole) contains references to one or more independent objects (the parts).   

class Library:
    def __init__(self, name):
        self.name = name  
        self.books = []
        
    def add_book(self, book):
         self.books.append(book)
         
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
        
class Book: 
    def __init__(self, title, author):
        self.title = title   
        self.author = author  
        
library = Library("Ali Awami Kitab Ghar")

book1 = Book("48 Laws of Power", "Robert Greene")
book2 = Book("The Art of Hacking with Ali", "Syed Ali Zaidi")
book3 = Book("Mastering DevOps With Production level Projects." , "Syed Ali Zaidi")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
# print(library.list_books())


for book in library.list_books(): 
    print(book)