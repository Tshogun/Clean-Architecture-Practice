from dataclasses import dataclass
from src.domain.value_objects.isbn import ISBN

@dataclass
class Book:
    """Entity representing a Book."""
    title: str
    author: str
    isbn: ISBN
    category: str 
    
    @classmethod
    def create(cls, title: str, author: str, isbn_str: str, category: str) -> 'Book':
        """Factory method to create a Book entity with validated ISBN."""
        isbn = ISBN(isbn_str)  
        return cls(title=title, author=author, isbn=isbn, category=category)