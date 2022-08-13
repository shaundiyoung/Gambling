from models import create_app, db
from flask import render_template, url_for, flash, request, redirect, session
from myforms import myForm, signUp

app = create_app()


@app.route('/', methods=["GET", "POST"])
def home():
    form = signUp()
    if form.validate_on_submit():
        flash(form.password.data)
        # return redirect('landing')
    return render_template("login.html", form=form)

@app.route('/landing')
def landing():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")