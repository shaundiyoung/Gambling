from models import create_app, db
from flask import render_template, url_for, flash, request, redirect, session
from myforms import myForm, signUp
from models import User

app = create_app()


@app.route('/', methods=["GET", "POST"])
def home():
    form = signUp()
    user = User.query.all()
    all_user = [(i.username, i.password) for i in user]
    if form.validate_on_submit():
        # flash(form.password.data)
        for i in all_user:
            if form.name.data == i[0]:
                flash("User Already Exists")
                redirect('/')
        if form.password1.data != form.password.data:
                flash("Passwords don't match")
                redirect('/')
        else:
            user = User(username=form.name.data, password=form.password.data)
            return redirect('login')

        # return redirect('landing')
    return render_template("signup.html", form=form)

@app.route('/landing')
def landing():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    form = myForm()
    user = User.query.all()
    all_user = [(i.username, i.password) for i in user]
    if form.validate_on_submit():
        for i in all_user:
            if form.name.data == i[0] and form.password.data == i[1]:
                return redirect('landing')
            elif form.name.data == i[0]:
                flash("Password Does Not Match")
        flash("user account does not exist")
            
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0")