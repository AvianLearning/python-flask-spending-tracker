from flask import Flask, render_template



app = Flask(__name__)

# register all the blueprints - company, tag, transaction

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()