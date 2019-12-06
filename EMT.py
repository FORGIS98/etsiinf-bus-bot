import requests
import shlex
import json

from subprocess import Popen, PIPE

# open json files
with open("buses.json") as f:
    data = json.load(f)

# constant url, do not change or everything stops working
URL = "http://api.interurbanos.welbits.com/v1/stop/"


def getAllBusTimes(stopNumber):
    """Returns a dictionary with (busNumber => time) to stopNumber"""
    busLines =  data[stopNumber]["bus"]

#    comando = "lwp-request " + URL + stopNumber
#    print("----------------->", comando)
#    args = shlex.split(comando)
#    proc = Popen(args, stdout=PIPE)
#    proc = Popen(args, stderr=PIPE)
#
#    output = proc.communicate()
#    print("OUTPUT :: ", output)

    req = requests.get(URL + stopNumber)
    req = json.loads(req.content)

    answer = {}

    for i in range (0, len(req["lines"])):
        aux = req["lines"][i]["lineNumber"]
        for j in range (0, len(busLines)):
            if(aux == busLines[j]):
                answer[busLines[j]] = req["lines"][i]["waitTime"]

    return answer




def main():
    print("Here we go!")
    res = getAllBusTimes("08771")

    for i in res:
        print(i, ":", res[i])

main()
