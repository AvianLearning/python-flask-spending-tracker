import pdb

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

from models.company import Company
import repositories.company_repository as company_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

transaction_repository.delete_all()
company_repository.delete_all()
tag_repository.delete_all()

company_1 = Company("RailScot")
company_repository.save(company_1)

company_2 = Company("Pilot Beer")
company_repository.save(company_2)

company_3 = Company("WideNation")
company_repository.save(company_3)

tag_1 = Tag("travel")
tag_repository.save(tag_1)

tag_2 = Tag("food")
tag_repository.save(tag_2)

tag_3 = Tag("mortgage")
tag_repository.save(tag_3)

transaction_1 = Transaction(150.00, company_1, tag_1)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(32.00, company_2, tag_2)
transaction_repository.save(transaction_2)

transaction_3= Transaction(750.00, company_3, tag_3)
transaction_repository.save(transaction_3)

pdb.set_trace()


