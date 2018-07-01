from mongoengine import *

class Order(Document):
    service_name = StringField()
    user_id = StringField()
    time = DateTimeField()
    is_accepted = BooleanField()