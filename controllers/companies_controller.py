from flask import Blueprint, Flask, redirect, render_template, request

from models.company import Company
import repositories.company_repository as company_repository

companies_blueprint = Blueprint("companies", __name__)

# Companies index
@companies_blueprint.route("/companies")
def companies():
    companies = company_repository.select_all()
    return render_template("companies/index.html", companies=companies)

