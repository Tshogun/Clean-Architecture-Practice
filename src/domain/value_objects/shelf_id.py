from dataclasses import dataclass
import uuid

@dataclass(frozen=True)
class ShelfID:
    """Value Object representing a Shelf ID."""
    shelf_id: str

    def __post_init__(self):
        """Validate the UUID format after initialization."""
        try:
            uuid_obj = uuid.UUID(self.id)
        except ValueError:
            raise ValueError(f"Invalid UUID format: {self.id}")