import requests
import json

url = 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/'

headers = {
    'email': 'cifradoforgis@gmail.com',
    'password': '',
    'X-ApiKey' : '',
    'X-ClientId' : ''
}

req = requests.get(url, headers=headers)
req = json.loads(req.content)
accessT = req["data"][0]["accessToken"]


url = 'https://openapi.emtmadrid.es/v1/transport/busemtmad/stops/383/detail/'
headers = {
    'accessToken': accessT,
}
req = requests.get(url, headers=headers)
req = json.loads(req.content)
print(req["data"][0]["stops"][0]["name"])
