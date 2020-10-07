from db.run_sql import run_sql
from models.budget import Budget

def save(budget):
    sql = "INSERT INTO budgets (total_budget) VALUES (%s) RETURNING id"
    values = [budget.total_budget]
    results = run_sql(sql, values)
    id = results[0]['id']
    budget.id = id

def select_all():
    budgets = []

    sql = "SELECT * FROM budgets"
    results = run_sql(sql)

    for result in results:
        budget = Budget(result['total_budget'], result['id'])
        budgets.append(budget)
    return budgets

def select(id):
    budget = None
    sql = "SELECT * FROM budgets WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = Budget(result['total_budget'], result['id'])
    return budget

def delete_all():
    sql = "DELETE from budgets"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM budgets WHERE id=%s"
    values = [id]
    run_sql(sql, values)


def update(budget):
    sql = "UPDATE budgets SET total_budget = %s WHERE id=%s"
    values = [budget.total_budget, budget.id]
    run_sql(sql, values)