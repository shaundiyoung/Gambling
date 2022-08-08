from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import devConfig

db = SQLAlchemy()


def create_app():
    app =Fl
    db.init_app(app)
    return app
