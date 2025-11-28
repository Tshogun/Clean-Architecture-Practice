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
    membership: Membership