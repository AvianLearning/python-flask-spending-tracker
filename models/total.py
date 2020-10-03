from models.transaction import *

transaction_1 = Transaction(10.00, "RailScot", "travel")
transaction_2 = Transaction(6.50, "Pilot Beer", "food")

all_transactions = [transaction_1, transaction_2]

def get_total(transactions):
    total = 0
    for transaction in transactions:
        total += transaction.amount
    return total

result = get_total(all_transactions)
print(result)