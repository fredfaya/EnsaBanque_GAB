import requests
import json


def getTransfert(ref, pin):
    api_url = "https://transfert-service-01.herokuapp.com/api/v0/transfer_service_api/UTransfer/pin_code/" + ref + "?code_pin=" + pin

    response = requests.get(api_url)
    if response.text == " wrong REFERENCE !":
        return "wrong reference"
    if response.text == " wrong PIN CODE !":
        return "wrong pin"
    if response.status_code == 500:
        return "server issue"

    return response.text


'''res = getTransfert("8374181449104","L49SgSoV")
res = json.loads(res)
print(res['transfers'][0]['amount'])'''
