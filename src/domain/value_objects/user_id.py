from dataclasses import dataclass
import uuid

@dataclass(frozen=True)
class UserID:
    """Value Object representing a User ID."""
    id: str

    def __post_init__(self):
        """Validate the UUID format after initialization."""
        try:
            uuid_obj = uuid.UUID(self.id)
        except ValueError:
            raise ValueError(f"Invalid UUID format: {self.id}")