from models import create_app, db
from flask import render_template, url_for, flash, request
from myforms import myForm, signUp

app = create_app()


@app.route('/', methods=["GET", "POST"])
def home():
    signUp = signUp()
    return render_template("login.html", signUp=signUp)

@app.route('/landing')
def landing():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")