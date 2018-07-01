from mongoengine import *


#1. Design Database
class Video(Document):
    title = StringField()
    thumbnail = StringField()
    views = IntField()
    link = StringField()
    youtube_id = StringField()
    

