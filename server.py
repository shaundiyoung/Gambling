from models import create_app, db, url_for
from flask import render_template

app = create_app()


@app.route('/')
def home():
    return "<h1>Hello World</h1>"

@app.route('/landing')
def landing():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()