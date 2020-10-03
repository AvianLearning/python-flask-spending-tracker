from db.run_sql import run_sql

from models.company import Company

def save(company):
    sql = "INSERT INTO companies (name) VALUES (%s) RETURNING id"
    values = [company.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    company.id = id


def select_all():
    companies = []

    sql = "SELECT * FROM companies"
    results = run_sql(sql)

    for result in results:
        company = Company(result['name'], result['id'])
        companies.append(company)
    return companies


def select(id):
    company = None
    sql = "SELECT * FROM companies WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        company = Company(result['name'], result['id'])
    return company


def delete_all():
    sql = "DELETE from companies"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM companies WHERE id=%s"
    values = [id]
    run_sql(sql, values)


def update(company):
    sql = "UPDATE companies SET name = %s WHERE id=%s"
    values = [company.name, company.id]
    run_sql(sql, values)