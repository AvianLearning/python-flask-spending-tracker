from flask import Flask, render_template

from controllers.transactions_controller import transactions_blueprint
from controllers.companies_controller import companies_blueprint
from controllers.tags_controller import tags_blueprint

app = Flask(__name__)

# register all the blueprints - company, tag, transaction
app.register_blueprint(transactions_blueprint)
app.register_blueprint(companies_blueprint)
app.register_blueprint(tags_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()