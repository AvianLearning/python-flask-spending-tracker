class Transaction:
    def __init__(self, amount, company, tag, id=None):
        self.amount = amount
        self.company = company
        self.tag = tag
        self.id = id

    def get_total(self, transactions):
        total = 0
        for transaction in transactions:
            total += transaction.amount
        return total

