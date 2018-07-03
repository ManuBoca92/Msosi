from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField
from wtforms.validators import  InputRequired, Email, Length, DataRequired, EqualTo




class UserRegForm(FlaskForm):
    firstName = StringField('first name ', validators=[InputRequired(), Length(max=50)])
    lastName = StringField('last name', validators=[InputRequired(), Length(max=50)])
    address = StringField('address', validators=[InputRequired(), Length(max=50)])
    city = StringField('city', validators=[InputRequired(), Length(max=50)])
    email = StringField('email', validators=[InputRequired(), Email('Email required'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50),
                                                     DataRequired(), EqualTo('confirm',
                                                    message='Passwords do no match!')])
    confirm = PasswordField('confirm password')