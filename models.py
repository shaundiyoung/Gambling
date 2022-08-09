from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import devConfig

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(devConfig())
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app


class User(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True, unique=True)
    score = db.Column(db.Float(), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username):
        self.username = username
        self.score = 0.0

    def __repr__(self):
        return '<User %r>' % self.username