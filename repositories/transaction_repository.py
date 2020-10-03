from db.run_sql import run_sql
from models.transaction import Transaction
from models.company import Company
from models.tag import Tag
import repositories.company_repository as company_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, company_id, tag_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.company.id, transaction.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id


def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        company = company_repository.select(result["company_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], company, tag, result["id"])
        transactions.append(transaction)
    return transactions


def select(id):
    sql = "SELECT * FROM transactions WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]
    company = company_repository.select(result["company_id"])
    tag = tag_repository.select(result["tag_id"])
    transaction = Transaction(result["amount"], company, tag, result["id"])
    return transaction


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions where id=%s"
    values = [id]
    run_sql(sql, values)