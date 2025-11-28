from dataclasses import dataclass
from enum import Enum
from datetime import date

class MembershipStatus(Enum):
    """Defines the possible states for a Membership."""
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'
    EXPIRED = 'expired'
    CANCELLED = 'cancelled'

@dataclass(frozen=True)
class Membership:
    """
    Value Object representing immutable Membership details.
    """
    status: MembershipStatus
    start_date: date  
    end_date: date
    
    def __post_init__(self):
        """Validate the business constraint: start date must precede end date."""
        if self.start_date >= self.end_date:
            raise ValueError("start_date must be strictly before end_date.")
            
    def is_temporally_valid_on(self, check_date: date) -> bool:
        """
        Check if the membership is valid based only on its date range, 
        regardless of its status (e.g., PENDING or INACTIVE).
        """
        return self.start_date <= check_date <= self.end_date

    def is_active(self, check_date: date) -> bool:
        """
        Check if the membership is both:
        1. Operationally 'ACTIVE' (status)
        2. Temporally valid (date range)
        """
        return (
            self.status == MembershipStatus.ACTIVE and 
            self.is_temporally_valid_on(check_date)
        )