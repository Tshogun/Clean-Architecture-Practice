from dataclasses import dataclass
import src.domain.value_objects.email as Email 
import src.domain.value_objects.user_id as UserID
import src.domain.value_objects.membership as Membership

@dataclass
class User:
    """Entity representing a User."""
    user_id: UserID
    name: str
    email: Email.Email
    address: str
    #active, inactive, pending, expired, cancelled
    #start date, end date, today's date as checking date
    membership: Membership  
    
    @classmethod
    def create(cls, user_id_str: str, name: str, email_str: str, address: str,
               membership_status: Membership.MembershipStatus,
               membership_start_date, membership_end_date) -> 'User':
        """Factory method to create a User entity with validated value objects."""
        user_id = UserID.UserID(user_id_str)  
        email = Email.Email(email_str)        
        membership = Membership.Membership(
            status=membership_status,
            start_date=membership_start_date,
            end_date=membership_end_date
        )  
        return cls(
            user_id=user_id,
            name=name,
            email=email,
            address=address,
            membership=membership
        )