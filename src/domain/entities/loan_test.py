from src.domain.entities.loan import Loan
from src.domain.entities.copy import Copy
from src.domain.entities.book import Book
from src.domain.entities.user import User
from src.domain.entities.loan import Loan
from src.domain.value_objects.transaction_id import TransactionID
from src.domain.entities.copy import Copy
from src.domain.entities.book import Book
from src.domain.entities.user import User
from src.domain.value_objects.loan_status import LoanStatus, LoanStatusEnum
from src.domain.value_objects.money import Money 
from src.domain.value_objects.copy_status import CopyStatus, CopyStatusEnum 
from src.domain.value_objects.user_id import UserID
from src.domain.value_objects.email import Email
from src.domain.value_objects.membership import Membership
from datetime import date, timedelta 

book = Book(
        title="The Pragmatic Programmer",
        author="Andrew Hunt",
        isbn="978-0134442651",
        category="Software Development"
    )

copy = Copy(
		copy_id = "58D5E212-165B-4CA0-909B-C86B9CEE0111",
		shelf_id = "58D5E212-165B-4CA0-909B-C86B9CEE0111",
		book = book,
		status = CopyStatus(CopyStatusEnum.AVAILABLE)
	)	

user_id = UserID("58D5E212-165B-4CA0-909B-C86B9CEE0111")
email = Email("johndow@gmail.com")
membership = Membership("active", start_date=date(2025,11,12), end_date=date(2025,12,12))

user = User(
		user_id = user_id,
		name = "John Dow",
		address = "5th Street",
		email = email,
		membership = membership
	)

transaction_id_vo = TransactionID("58D5E212-165B-4CA0-909B-C86B9CEE0111")
status_vo = LoanStatus(LoanStatusEnum.ACTIVE)

def test_loan_direct_creation():
	"""Testing the direct instantiatino of loan entity"""
	start_dt = date(2025, 11, 23)
	duration_days = 14
	late_fee_vo = Money(0.0)
	expected_end_date = start_dt + timedelta(days = duration_days)

	loan = Loan.create(
        	transaction_id = transaction_id_vo,
        	copy = copy,
        	user = user,
        	start_date = start_dt,
        	duration = duration_days,
        	status = status_vo,
        	late_fee = late_fee_vo
    	)

	assert loan.end_date == expected_end_date
	assert loan.transaction_id is transaction_id_vo
	assert loan.copy is copy 
	assert loan.user is user
	assert loan.start_date == date(2025,11,23)
	assert loan.duration == 14
	assert loan.status is status_vo
	assert loan.late_fee == Money(0.0)