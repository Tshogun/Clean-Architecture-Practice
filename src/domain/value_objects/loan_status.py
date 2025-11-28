from dataclasses import dataclass
from enum import Enum

class LoanStatusEnum(Enum):
    """Enumeration for possible loan statuses."""
    ACTIVE = "active"
    RETURNED = "returned"
    OVERDUE = "overdue"

@dataclass(frozen=True)
class LoanStatus:
    """Value object representing the status of a loan."""
    status: LoanStatusEnum
    
    def __post_init__(self):
        """Validate the loan status after initialization."""
        if not isinstance(self.status, LoanStatusEnum):
            raise ValueError(f"Invalid loan status: {self.status}")