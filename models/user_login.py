from mongoengine import Document, EmailField, DateTimeField, StringField
from flask_login import UserMixin
from flask_mongoengine import BaseQuerySet


class UserLogin(UserMixin, Document):
    meta = {'collection': 'userLogin', 'queryset_class': BaseQuerySet}
    email = EmailField(max_length=50, required=True)
    password = StringField(max_length=20, required=True, validation=True)
