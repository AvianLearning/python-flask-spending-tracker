import unittest
from models.transaction import Transaction


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction_1 = Transaction(10.00, "RailScot", "travel")
        self.transaction_2 = Transaction(6.50, "Pilot Beer", "food")

    def test_transaction_has_amount(self):
        pass

    def test_transaction_has_company(self):
        pass

    def test_transaction_has_category(self):
        pass

    def test_can_return_total_of_transactions(self):
        pass