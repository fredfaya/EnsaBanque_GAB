import requests


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


def serve_transfert(ref):
    api_url = "https://transfert-service-01.herokuapp.com/api/v0/transfer_service_api/UTransfer/serve/" + ref
    response = requests.put(api_url)

    if response.status_code == 200:
        return True
    else:
        return "error"

'''res = getTransfert("8371994824481","BaV8lnf1")
res = json.loads(res)
print(res['transfers'][0]['amount'])'''
