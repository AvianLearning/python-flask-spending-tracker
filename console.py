import pdb

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

from models.company import Company
import repositories.company_repository as company_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.budget import Budget
import repositories.budget_repository as budget_repository

transaction_repository.delete_all()
company_repository.delete_all()
tag_repository.delete_all()
budget_repository.delete_all()

total_budget = Budget(0.00)
budget_repository.save(total_budget)

company_1 = Company("RailScot")
company_repository.save(company_1)

company_2 = Company("Pilot Beer")
company_repository.save(company_2)

company_3 = Company("WideNation")
company_repository.save(company_3)

company_4 = Company("Blub")
company_repository.save(company_4)

company_5 = Company("Amoosin Primula")
company_repository.save(company_5)

company_6 = Company("Blumen Ecke")
company_repository.save(company_6)

company_7 = Company("Cheeses of Nazareth")
company_repository.save(company_7)

company_8 = Company("Hair Today, Gone Tomorrow")
company_repository.save(company_8)

tag_1 = Tag("travel")
tag_repository.save(tag_1)

tag_2 = Tag("food")
tag_repository.save(tag_2)

tag_3 = Tag("mortgage")
tag_repository.save(tag_3)

tag_4 = Tag("utilities")
tag_repository.save(tag_4)

tag_5 = Tag("entertainment")
tag_repository.save(tag_5)

tag_6 = Tag("floristry")
tag_repository.save(tag_6)

tag_7 = Tag("personal")
tag_repository.save(tag_7)

transaction_1 = Transaction(150.00, company_1, tag_1)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(32.00, company_2, tag_2)
transaction_repository.save(transaction_2)

transaction_3 = Transaction(750.00, company_3, tag_3)
transaction_repository.save(transaction_3)

transaction_4 = Transaction(70.34, company_4, tag_4)
transaction_repository.save(transaction_4)

transaction_5 = Transaction(8.50, company_5, tag_5)
transaction_repository.save(transaction_5)

transaction_6 = Transaction(28.99, company_6, tag_6)
transaction_repository.save(transaction_6)

transaction_7 = Transaction(14.40, company_7, tag_2)
transaction_repository.save(transaction_7)

transaction_8 = Transaction(19.99, company_8, tag_7)
transaction_repository.save(transaction_8)

transactions = transaction_repository.select_all()


pdb.set_trace()


