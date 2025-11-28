from dataclasses import dataclass
from datetime import date, timedelta
import src.domain.value_objects.transaction_id as TransactionID
import src.domain.entities.copy as Copy
import src.domain.entities.user as User
import src.domain.value_objects.money as Money
import src.domain.value_objects.loan_status as LoanStatus

@dataclass(frozen=True)
class Loan:
    """Entity representing a Loan."""
    transaction_id: TransactionID
    copy: Copy
    user: User
    start_date: date 
    duration: int  
    end_date: date 
    status: LoanStatus
    late_fee: Money
    
    @classmethod
    def create(cls, transaction_id: TransactionID, copy: Copy, user: User,  start_date: date, duration: int, 
               status: LoanStatus, late_fee: Money) -> 'Loan':
        """Factory method to create a new Loan instance."""
        end_date = start_date + timedelta(days=duration)
        return cls(
            transaction_id=transaction_id,
            copy=copy,
            user=user,
            start_date=start_date,
            duration=duration,
            end_date=end_date,
            status=status,
            late_fee=late_fee
        )