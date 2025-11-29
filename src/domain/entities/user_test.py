from src.domain.entities.user import User 
from src.domain.value_objects.email import Email
from src.domain.value_objects.user_id import UserID
from src.domain.value_objects.membership import Membership
from datetime import date 

user_id = UserID("58D5E212-165B-4CA0-909B-C86B9CEE0111")
email = Email("johndow@gmail.com")
membership = Membership("active", start_date=date(2025,11,12), end_date=date(2025,12,12))

def test_user_direct_creation():
	"""Test the direct instantiation of user with user Id, email, address and membership"""
	user = User(
		user_id = user_id,
		name = "John Dow",
		address = "5th Street",
		email = email,
		membership = membership
	)

	assert user.user_id is user_id
	assert user.name is "John Dow"
	assert user.email is email
	assert user.address is "5th Street"
	assert user.membership is membership