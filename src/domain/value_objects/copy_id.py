from dataclasses import dataclass
import uuid

#   Note from Author: We can enter any specific Id formats as 
#   per the domain requirements. Here, we are using UUID as 
#   an example.

@dataclass(frozen=True)
class CopyID:
    """Value Object representing a Copy ID."""
    copy_id: str

    def __post_init__(self):
        """Validate the UUID format after initialization."""
        try:
            uuid_obj = uuid.UUID(self.id)
        except ValueError:
            raise ValueError(f"Invalid UUID format: {self.id}")