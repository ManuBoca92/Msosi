from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField
from wtforms.validators import  InputRequired, Email, Length, EqualTo, DataRequired




class UserLoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email('Email required'), Length(max=50)])
    # password =PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50),
                                                     DataRequired(), EqualTo('confirm',
                                                                             message='Passwords do no match!')])