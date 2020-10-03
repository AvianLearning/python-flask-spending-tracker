from flask import Blueprint, Flask, redirect, render_template, request

from models.company import Company
import repositories.company_repository as company_repository

companies_blueprint = Blueprint("companies", __name__)

# Companies index
@companies_blueprint.route("/companies")
def companies():
    companies = company_repository.select_all()
    return render_template("companies/index.html", companies=companies)

# Add company
@companies_blueprint.route("/companies/add")
def add_company():
    return render_template("companies/add.html")

# Create and return to companies page ??
@companies_blueprint.route("/companies", methods=["POST"])
def create_company():
    name = request.form["name"]
    new_company = Company(name)
    company_repository.save(new_company)
    return redirect("/companies")

# Edit company
@companies_blueprint.route("/companies/<id>/edit")
def edit_company(id):
    company = company_repository.select(id)
    return render_template("companies/edit.html", company=company)

# Update company and return to companies landing page
@companies_blueprint.route("/companies/<id>", methods=["POST"])
def update_company(id):
    name = request.form["name"]
    company = Company(name, id)
    company_repository.update(company)
    return redirect("/companies")

