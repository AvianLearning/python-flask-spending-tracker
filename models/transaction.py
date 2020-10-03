class Transaction:
    def __init__(self, amount, company, category, id=None):
        self.amount = amount
        self.company = company
        self.category = category
        self.id = id
