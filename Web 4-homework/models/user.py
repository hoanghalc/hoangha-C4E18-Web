from mongoengine import *

#1. Design Database
class User(Document):
    username = StringField()
    fullname = StringField()
    email = StringField()
    password = StringField()
    