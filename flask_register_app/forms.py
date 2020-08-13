from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=20)])
    remember_me = BooleanField('remember_me', validators=[])


class RegisterForm(LoginForm):
    full_name = StringField('full_name', validators=[DataRequired(), Length(min=3, max=100)])
    confirm_password = PasswordField('confirm_password', validators=[
        DataRequired(), Length(min=6, max=20), EqualTo('password', message='Passwords are not equal!')
    ])
    terms = BooleanField('terms', validators=[DataRequired()])
