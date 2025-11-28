from dataclasses import dataclass
import uuid

@dataclass(frozen=True)
class UserID:
    """Value Object representing a User ID."""
    user_id: str

    def __post_init__(self):
        """Validate the UUID format after initialization."""
        try:
            uuid_obj = uuid.UUID(self.user_id)
        except ValueError:
            raise ValueError(f"Invalid UUID format: {self.user_id}")