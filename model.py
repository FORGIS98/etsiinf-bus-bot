import requests
import json

# Web page: https://busmadrid.welbits.com/
URL = "http://api.interurbanos.welbits.com/v1/stop/"

def apiCall(stops, lines):
    answer = {}
    for l in lines:
        answer[l] = []

    i = 0 # += 1 if we don't get a 500
    while i < len(stops):
        req = requests.get(URL + stops[i])
        if(req.status_code != 500):
            req = json.loads(req.content)
            i += 1

            for data in req["lines"]:
                if(data["lineNumber"] in lines):
                    answer[data["lineNumber"]].append(data["waitTime"])

    return answer


def getEtsiinf():
    stops = ["08771", "17573", "08411"]
    lines = ["566", "571", "573", "591", "865"]
    return apiCall(stops, lines)

def getColonia():
    stops = ["08409"]
    lines =  ["571", "573", "591"]
    return apiCall(stops, lines)

def getAluche():
    stops = ["15782", "08380"]
    lines =  ["571", "591"]
    return apiCall(stops, lines)

def getMoncloa():
    stops = ["11278"]
    lines =  ["573","865"]
    return apiCall(stops, lines)
