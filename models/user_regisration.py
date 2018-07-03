from mongoengine import Document, EmailField, DateTimeField, StringField
from flask_mongoengine import BaseQuerySet
from flask_login import UserMixin


class UserRegistration(UserMixin, Document):
    meta = {'collection': 'userRegistration', 'queryset_class': BaseQuerySet}
    firstName = StringField(max_length=20, required=True)
    lastName = StringField(max_length=20, required=True)
    address = StringField(max_length=50, required=True)
    city = StringField(max_length=20, required=True)
    email = EmailField(max_length=50, required=True)
    password = StringField(max_length=50, required=True)
    confirm = StringField(max_length=50, required=True)