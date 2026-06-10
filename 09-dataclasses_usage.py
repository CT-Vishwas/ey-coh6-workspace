# Traditional way
# class Book:
#     def __init__(self, title:str, author:str,pages:int):
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def __repr__(self):
#         return f"Book(title={self.title}, author={self.author}, pages={self.pages})"
    
#     def __eq__(self, other):
#         if not isinstance(other, Book):
#             return f"Not a Book"
#         return (self.title, self.author, self.pages) == (other.title,other.author,other.pages)


# New way
from dataclasses import dataclass

@dataclass
class Book:
    title: str = "UNKNOWN"
    author: str = "UNKNOWN"
    pages: int = 0


book1 = Book("Pride and Prejudice", "Jane Austen", 200)
print(book1)
book2 = Book("Pride and Prejudice", "Jane Austen", "200")
print(book1 == book2)
