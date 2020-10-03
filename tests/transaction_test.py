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
        self.assertEqual(10.00, self.transaction_1.amount)

    def test_transaction_has_company(self):
        self.assertEqual("RailScot", self.transaction_1.company.name)

    def test_transaction_has_category(self):
        self.assertEqual("food", self.transaction_2.tag.category)

    # def test_can_return_total_of_transactions(self):
    #     # all_transactions = [self.transaction_1.amount, self.transaction_2.amount]
    #     # total = get_total(all_transactions)
    #     # self.assertEqual(16.50, total)