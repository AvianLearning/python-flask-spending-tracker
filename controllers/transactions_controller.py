from flask import Blueprint, Flask, redirect, render_template, request

from models.transaction import Transaction
from models.budget import Budget
import repositories.transaction_repository as transaction_repository
import repositories.company_repository as company_repository
import repositories.tag_repository as tag_repository
import repositories.budget_repository as budget_repository

transactions_blueprint = Blueprint("transactions", __name__)

# Index - show all transactions
@transactions_blueprint.route("/")
def transactions():
    transactions = transaction_repository.select_all()
    budget = budget_repository.select(1)
    
    total = round(get_total(transactions), 2)
    return render_template("index.html", all_transactions=transactions, total=total, budget=budget)


# Add transaction
@transactions_blueprint.route("/add-transaction")
def add_transaction():
    companies = company_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("add-transaction.html", companies=companies, tags=tags)

# Create transaction and redirect to home
@transactions_blueprint.route("/add-transaction/new", methods=["POST"])
def create_transaction():
    amount = request.form["amount"]
    company_id = request.form["company_id"]
    tag_id = request.form["tag_id"]
    company = company_repository.select(company_id)
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(amount, company, tag)
    transaction_repository.save(new_transaction)
    return redirect("/")

def get_total(transactions):
    total = 0.00
    for transaction in transactions:
        total += float(transaction.amount)
    return total

    
# Show budget
@transactions_blueprint.route("/")
def add_budget():
    budget = budget_repository.select_all()
    return render_template("index.html", budget=budget)

# Add budget and return to home
@transactions_blueprint.route("/budget/edit", methods=["POST"])
def create_budget():
    budget = request.form["budget"]
    new_budget = Budget(budget, 1)
    budget_repository.update(new_budget)
    return redirect("/")



# @transactions_blueprint.route("/", methods=["POST"])
# def create_budget():
#     budget = request.form["budget"]
#     return redirect("/", budget=budget)

# Ask instructor




# Method to create budget and warn user if over budget:

# Enter budget - form field
# Use get total spend method to compare to budget
# If budget is within £100 of total spend
# Display budget as red text
# Otherwise display budget as green text

# def warn_near_budget():
#     budget = request.form["budget"]
#     total = get_total(transactions)

#     if total >= (budget - 100):
#         return True
#     else
#         return False