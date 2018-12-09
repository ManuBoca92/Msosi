from mongoengine import Document, StringField, ImageField
from flask_login import UserMixin
from flask_mongoengine import BaseQuerySet


class Menu(UserMixin, Document):
    meta = {'collection': 'Menu', 'queryset_class': BaseQuerySet}
    menu_name = StringField(max_length=50, required=True)
    menu_image = ImageField(max_length=20, required=True)
    menu_description = StringField(max_length=150, required=True)
