import requests
import json
import time

def createSound(speak):
    url = "https://api.soundoftext.com/sounds/"
    headers = {'Content-type': 'application/json'}
    status = "Pending"
    data = json.dumps({"engine": "Google","data": {"text": speak,"voice": "de-DE"}})
    response = requests.post(url, data=data, headers=headers)
    id=response.json()['id']
    while(status=="Pending"):
        response = requests.get(url + id, data=None, headers=headers)
        status=response.json()['status']
        if(status=="Pending"):
          time.sleep(10)
    response = requests.get(url + id, data=None, headers=headers)
    location = response.json()['location']
    return location

#if __name__ == '__main__':
#    print(createSound("Hallo Welt!"))
