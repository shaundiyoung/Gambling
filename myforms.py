from ast import Pass
from tokenize import String
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, NumberRange, EqualTo
from flask_wtf import FlaskForm




class myForm(FlaskForm):
    name = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])

class signUp(FlaskForm):
    name = StringField("name: ", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('password1', message='Names must match')])
    password1 = PasswordField("Confirm Password:")