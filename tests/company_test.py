import unittest
from models.company import Company

class TestCompany(unittest.TestCase):

    def setUp(self):
        self.company = Company("WideNation")

    def test_company_has_name(self):
        self.assertEqual("WideNation", self.company.name)
