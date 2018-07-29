import requests
import json

def post():
    url = "http://127.0.0.1:5000"
    postDict = {
        "userName": "98997",
        "disc": "hudihiudhu",
        "expDate":"2",
        "data": [
        "10.10",
        "10.11",
        "11.3"
        ]
    }
    headers = {'Content-Type':'application/json'}
    r = requests.post(url, headers=headers, data = json.dumps(postDict))
    print(r.json())

if __name__ == '__main__':
    post()
