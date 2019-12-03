import requests
import json
import os

url = 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/'
urlInter = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last/'


headers = {
    'email': 'cifradoforgis@gmail.com',
    'password': os.environ["passwdEMT"],
    'X-ApiKey' : os.environ["EMT_KEY"],
    'X-ClientId' : os.environ["EMT_ClientId"],
}

req = requests.get(url, headers=headers)
req = json.loads(req.content)
accessT = req["data"][0]["accessToken"]


url = urlInter + 'bus/GetTimesLines.php'
headers = {
    # 'accessToken': accessT,
    'passKey' : os.environ["EMT_KEY"],
    'idClient' : os.environ["EMT_ClientId"],
    'SelectDate' : '03/12/2019',
    'lines' : '08411'
}

req = requests.post(url, headers=headers)
req = json.loads(req.content)
print(req)
