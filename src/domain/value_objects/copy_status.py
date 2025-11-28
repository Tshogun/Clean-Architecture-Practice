from dataclasses import dataclass
from enum import Enum

class CopyStatusEnum(Enum):
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"
    RESERVED = "reserved"
    LOST = "lost"
    
@dataclass(frozen=True)
class CopyStatus:
    """Value Object representing the status of a Copy."""
    status: CopyStatusEnum
    
  