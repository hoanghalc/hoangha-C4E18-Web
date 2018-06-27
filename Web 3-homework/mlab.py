import mongoengine

# mongodb://c4e18:hoanghalc96@ds163700.mlab.com:63700/muadongkhonglanh-c4e18

host = "ds163700.mlab.com"
port = 63700
db_name = "muadongkhonglanh-c4e18"
user_name = "c4e18"
password = "hoanghalc96"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())