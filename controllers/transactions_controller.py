from flask import Blueprint, Flask, redirect, render_template, request

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.company_repository as company_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

# Index - show all transactions
@transactions_blueprint.route("/")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("index.html", all_transactions=transactions)


# Add transaction
@transactions_blueprint.route("/add-transaction")
def add_transaction():
    companies = company_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("add-transaction.html", companies=companies, tags=tags)

# Create transaction and redirect to home
@transactions_blueprint.route("/", methods=["POST"])
def create_transaction():
    amount = request.form["amount"]
    company_id = request.form["company_id"]
    tag_id = request.form["tag_id"]
    company = company_repository.select(company_id)
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(amount, company, tag)
    transaction_repository.save(new_transaction)
    return redirect("/")

