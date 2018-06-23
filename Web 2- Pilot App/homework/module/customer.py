from mongoengine import *


#1. Design Database
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()

