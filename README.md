# Cash Flow spending tracker #

### Python/Flask app for CodeClan solo project. ###
### Brief was to build a full-stack app that enables a user to track their spending.

#### Features ####
* Shows user transactions in a single view, with each transaction's amount, merchant and spend category, and a total for all transactions.
* Shows a total budget and warns user if getting within £100 of budget.

#### Instructions to run ####
* Ensure to have the current version of Python, Flask, and PostGres installed.
* In terminal, navigat to the project folder.
* Run the following commands in terminal: 
  * psql -d spending_tracker -f spending_tracker.sql 
  * python3 console.py
* Then open your browser to your Flask port (default: http://localhost:5000/)
