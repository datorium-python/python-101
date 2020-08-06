from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email, DataRequired


class BasicForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    first_name = StringField('First Name', validators=[Length(min=3, max=50)])
    last_name = StringField('Last Name', validators=[Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])