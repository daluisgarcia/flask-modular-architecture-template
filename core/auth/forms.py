from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import validators


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[validators.data_required(), validators.length(min=4, max=40)])
    password = PasswordField('Password', validators=[validators.data_required()])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.data_required(), validators.length(min=4, max=40)])
    password = PasswordField('Password', validators=[validators.data_required()])
    remember_me = BooleanField('Remember me', default=False, validators=[validators.optional()])
