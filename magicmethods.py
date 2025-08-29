# Magic Method ->> Dundar Merthods (double underscore) , __init__, __str__, __eq__ 
# They are automatically called by many of Python's built-in operations.  
# They allow developers to define or customize the behaviour of the objects.  

class Book: 
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author 
        self.num_pages = num_pages 
        
    def __str__(self):
        return f"{self.title} by {self.author}" 
    
    def __eq__(self, other): ##other for two other books 
        return self.title == other.title and self.author == other.author 
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages 
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages 
    
    def __add__(self,other):
        return f"{self.num_pages + other.num_pages } pages"
    
    def __contains__(self, keyword): 
        return keyword in self.title or keyword in self.author 
    
    def __getitem__(self, key):
        if key == "title":
            return self.title 
        elif key == "author": 
            return self.author 
        elif key == "num_pages":
            return self.num_pages
        else: 
            return f"Key {key} was not found"
        
        
    
book1 = Book("48 Laws of Power", "Robert Greene" , 270)
book2 = Book("Advance Python", "Lary Grey", 342)
book3 = Book("Master gRpc with Golang", "William Kennedy", 220)

print(book3)