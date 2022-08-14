from models import create_app, db
from flask import render_template, url_for, flash, request, redirect, session, jsonify
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
            db.session.add(user)
            db.session.commit()
            return redirect('login')

        # return redirect('landing')
    return render_template("signup.html", form=form)

@app.route('/landing')
def landing():
    if "user" not in session:
        return redirect('login')
    else:
        user = User.query.filter_by(username=session['user']).first()
        return render_template("index.html", user=user)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = myForm()
    user = User.query.all()
    all_user = [(i.username, i.password) for i in user]
    if form.validate_on_submit():
        for i in all_user:
            if form.name.data == i[0] and form.password.data == i[1]:
                session["user"] = i[0]
                return redirect('landing')
        flash("Incorrect Password or Username")
            
    return render_template("login.html", form=form)

@app.route('/board')
def board():
    if "user" not in session:
        return redirect('login')
    else:
        userdata = User.query.all()
        userdata = [(i.username, i.score) for i in userdata]
        userdata = sort_tuple_list(userdata)
        return render_template("board.html", userdata=userdata)


@app.route('/api/add/<amount>', methods=["GET", "POST"])
def add(amount):
    if request.method == "POST":
        if "user" not in session:
            return {"error":"User Not logged In"}
        elif int(amount)>0:
            user = User.query.filter_by(username=session['user']).first()
            user.score = int(user.score) + int(amount)
            db.session.commit()
            return jsonify({"newscore":user.score})
        else:
            return jsonify({"Invalid":" Amount"})
    else:
        return jsonify({"Method": "incorrect"})

@app.route('/api/sub/<amount>', methods=["GET", "POST"])
def sub(amount):
    if request.method == "POST":
        if "user" not in session:
            return {"error":"User Not logged In"}
        elif int(amount)>0:
            user = User.query.filter_by(username=session['user']).first()
            user.score = int(user.score) - int(amount)
            db.session.commit()
            return jsonify({"newscore":user.score})
        else:
            return jsonify({"Invalid":" Amount"})
    else:
        return jsonify({"Method": "incorrect"})

@app.route('/logout')
def logout():
    if "user" in session:
        session.pop("user")
        return redirect("login")
    else:
        return redirect("login")

def sort_tuple_list(tuplelist):
    tuplelist.sort(key = lambda x: x[1])
    print(tuplelist)
    return tuplelist

if __name__ == '__main__':
    app.run(host="0.0.0.0")