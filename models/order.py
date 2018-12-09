from mongoengine import Document, StringField, ImageField, IntField, DateTimeField
from flask_login import UserMixin
from flask_mongoengine import BaseQuerySet


class Order(UserMixin, Document):
    meta = {'collection': 'Order', 'queryset_class': BaseQuerySet}
    user_id = IntField(required=True)
    order_quantity = IntField(required=True)
    order_price = IntField(required=True)
    order_date = DateTimeField()
    status = StringField(required=True)
    payment_method = StringField(max_length=100, required=True)
