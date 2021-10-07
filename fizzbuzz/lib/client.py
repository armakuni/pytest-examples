import requests


class Client(object):
    def __init__(self, api_url):
        self.api_url = api_url

    def fizzbuzz(self, input):
        result = requests.get(f"{self.api_url}/fizzbuzz/{input}").content
        return result.decode(encoding="utf-8")
