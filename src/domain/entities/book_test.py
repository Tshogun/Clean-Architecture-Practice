from src.domain.entities.book import Book 
from src.domain.value_objects.isbn import ISBN

VALID_ISBN_STRING = "978-0134442651"
INVALID_ISBN_STRING = "123-INVALID-456"
valid_isbn_vo = ISBN(VALID_ISBN_STRING)

def test_book_direct_creation():
    """Tests direct instantiation with an existing ISBN Value Object."""
    book = Book(
        title="The Clean Coder",
        author="Robert C. Martin",
        isbn=valid_isbn_vo,
        category="Software Engineering"
    )
    assert book.title == "The Clean Coder"
    assert book.author == "Robert C. Martin"
    assert book.isbn is valid_isbn_vo 
    assert book.category == "Software Engineering"

def test_book_equality_and_difference():
    """Tests entity equality based on attributes (standard dataclass behavior)."""
    book1 = Book("Title", "Author", valid_isbn_vo, "Cat")
    book2 = Book("Title", "Author", valid_isbn_vo, "Cat")
    book3 = Book("Title Diff", "Author", valid_isbn_vo, "Cat")
    
    assert book1 == book2
    assert book1 != book3
    
def test_book_factory_method_with_valid_isbn():
    """Tests the factory method for creating a Book with a valid ISBN string."""
    book = Book.create(
        title="Clean Architecture",
        author="Robert C. Martin",
        isbn_str=VALID_ISBN_STRING,
        category="Software Engineering"
    )
    assert book.title == "Clean Architecture"
    assert book.author == "Robert C. Martin"
    assert book.isbn == valid_isbn_vo
    assert book.category == "Software Engineering"
    
def test_book_factory_method_with_invalid_isbn():
    """Tests that the factory method raises an error with an invalid ISBN string."""
    try:
        Book.create(
            title="Invalid Book",
            author="Unknown",
            isbn_str=INVALID_ISBN_STRING,
            category="Unknown"
        )
        assert False
    except ValueError as e:
        assert str(e) == f"Invalid ISBN format: {INVALID_ISBN_STRING}"
        
def test_book_is_mutable():
    """
    Tests that the Book entity is mutable.
    """
    book = Book(
        title="Old Title",
        author="Old Author",
        isbn=valid_isbn_vo,
        category="Old Category"
    )
    
    new_isbn = ISBN("978-0321125217")
    book.title = "New Title"
    book.isbn = new_isbn
    
    assert book.title == "New Title"
    assert book.isbn is new_isbn
    assert id(book) == id(book)