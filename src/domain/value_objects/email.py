from dataclasses import dataclass 
import re

@dataclass(frozen=True)
class Email:
    """Validate Object representing an Email Address."""
    email_address: str
    
    def __post_init__(self):
        """Validate the email address format after initialization."""
        if not self.is_valid(self.email_address):
            raise ValueError(f"Invalid email address format: {self.email_address}")
    
    @staticmethod
    def is_valid(email_address: str) -> bool:
        """Validates the email address format."""
        format = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(format, email_address):
            return False
        return True