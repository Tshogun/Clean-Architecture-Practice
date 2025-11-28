from dataclasses import dataclass

@dataclass(frozen=True)
class ISBN:
    """Value object representing an ISBN (International Standard Book Number)."""
    ISBN: str
    
    def __post_init__(self):
        """Validate the ISBN format after initialization."""
        if not self.is_valid(self.ISBN):
            raise ValueError(f"Invalid ISBN format: {self.ISBN}")
    
    @staticmethod
    def is_valid(ISBN: str) -> bool:
        """Validate the ISBN-10 or ISBN-13 format."""
        return len(ISBN.replace("-", "").replace(" ", "")) in (10, 13)