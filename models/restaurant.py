from mongoengine import Document, EmailField, DateTimeField, StringField, IntField
from flask_mongoengine import BaseQuerySet
from flask_login import UserMixin


class Restaurant(UserMixin, Document):
    meta = {'collection': 'Restaurant', 'queryset_class': BaseQuerySet}
    name = StringField(max_length=20, required=True)
    description = StringField(max_length=20, required=True)
    address = StringField(max_length=100, required=True)
    city = StringField(max_length=20, required=True)
    email = EmailField(max_length=50, required=True)
    phone = IntField(max_length=50, required=True)
    opening_time = DateTimeField(max_length=50, required=True)
    closing_time = DateTimeField()