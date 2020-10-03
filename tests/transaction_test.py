import unittest
from models.transaction import Transaction
from models.company import Company
from models.tag import Tag

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.company_1 = Company("RailScot")
        self.tag_1 = Tag("travel")
        self.company_2 = Company("Pilot Beer")
        self.tag_2 = Tag("food")

        self.transaction_1 = Transaction(10.00, self.company_1, self.tag_1)
        self.transaction_2 = Transaction(6.50, self.company_2, self.tag_2)

    def test_transaction_has_amount(self):
        pass

    def test_transaction_has_company(self):
        pass

    def test_transaction_has_category(self):
        pass

    def test_can_return_total_of_transactions(self):
        pass