from dataclasses import dataclass
from src.domain.value_objects.copy_id import CopyID
from src.domain.entities.book import Book
from src.domain.value_objects.shelf_id import ShelfID
from src.domain.value_objects.copy_status import CopyStatus

@dataclass
class Copy:
    """Entity representing a Copy in the system."""
    copy_id: CopyID
    book: Book
    shelf_id: ShelfID
    status: CopyStatus
    
    @classmethod
    def create(cls, copy_id: CopyID, book: Book, shelf_id: ShelfID, status: CopyStatus) -> 'Copy':
        """Factory method to create a new Copy instance."""
        return cls(copy_id=copy_id, book=book, shelf_id=shelf_id, status=status)