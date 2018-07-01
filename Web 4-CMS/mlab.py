import mongoengine

# mongodb://cms:hoanghalc96@ds121371.mlab.com:21371/cms-c4e18

host = "ds121371.mlab.com"
port = 21371
db_name = "cms-c4e18"
user_name = "cms"
password = "hoanghalc96"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())