import requests
import json

url ="http://127.0.0.1:8000/student/"

def data_get(id=None):
    try:
        data = {}
        if id!= None:
            data = {'id':id}
        json_data = json.dumps(data)
        r = requests.get(url = url , data=json_data)
        data = r.json()
        print(data)

    except Exception as e:
        print(e)
# data_get(2)


def post_data():
    data = {
        'name':'mona',
        'roll_no':104,
        'city': 'khejroli',
        'contect_no': 234234335
    }
    json_data = json.dumps(data)
    r = requests.post(url = url , data=json_data)
    data = r.json()
    print(data)
# post_data()   

def update_data():
    data = {
        'id':4,
        'name':'monika',
        'roll_no':134,
    }
    json_data = json.dumps(data)
    r = requests.put(url = url , data=json_data)
    data = r.json()
    print(data)

update_data()

def delete_data():
    data = {'id':3}
    json_data = json.dumps(data)
    r = requests.delete(url = url , data=json_data)
    data = r.json()
    print(data)
# delete_data()