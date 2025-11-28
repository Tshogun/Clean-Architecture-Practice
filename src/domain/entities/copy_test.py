from src.domain.entities.copy import Copy
from src.domain.value_objects.copy_id import CopyID
from src.domain.entities.book import Book
from src.domain.value_objects.shelf_id import ShelfID
from src.domain.value_objects.copy_status import CopyStatus

def test_copy_direct_creation():
    """Tests direct instantiation with existing Value Objects."""
    copy_id_vo = CopyID("58D5E212-165B-4CA0-909B-C86B9CEE0111")
    shelf_id_vo = ShelfID("58D5E212-165B-4CA0-909B-C86B9CEE0211")
    status_vo = CopyStatus("available")
    book = Book(
        title="The Pragmatic Programmer",
        author="Andrew Hunt",
        isbn=None,
        category="Software Development"
    )
    
    copy = Copy(
        copy_id=copy_id_vo,
        book=book,
        shelf_id=shelf_id_vo,
        status=status_vo
    )
    
    assert copy.copy_id is copy_id_vo
    assert copy.book is book
    assert copy.shelf_id is shelf_id_vo
    assert copy.status is status_vo