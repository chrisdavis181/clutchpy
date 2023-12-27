import requests
from requests.auth import HTTPBasicAuth
import json

class Client:
    def __init__(self, base_url, brand, location, terminal, key, secret, timeout, env):
        self.base_url = base_url
        self.key = key
        self.secret = secret
        self.location = location
        self.terminal = terminal
        self.brand = brand
        self.timeout = timeout
        self.env=env
        self.auth = HTTPBasicAuth(self.key, self.secret)
        
    def set_headers(self, headers):
        required_headers = {
            'location': self.location,
            'terminal': self.terminal,
            'brand': self.brand
        }

        required_headers.update(headers)
        return required_headers

    def post(self, url, params={}, headers={}):
        return requests.post(url=url, data=params, headers=headers, timeout=self.timeout, auth=self.auth)

    def request(self, method, path, params={}, headers={}):
        headers = self.set_headers(headers)
        url = self.base_url + path
        method = getattr(self, method)
        return method(url, params=json.dumps(params), headers=headers)
