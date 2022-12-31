import requests
import json


class DataManager:
    def __init__(self,
                 api_url):
        self.api_url = api_url

    def getData(self):
        response_API = requests.get(self.api_url)
        print(response_API.status_code)
        data = response_API.text
        parse_json = json.loads(data)
        info = parse_json['description']
        print("Info about API:\n", info)
        key = parse_json['parameters']['key']['description']
        print("\nDescription about the key:\n", key)
