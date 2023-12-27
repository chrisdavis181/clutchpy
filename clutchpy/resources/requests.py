class Requests:
    def __init__(self, client):
        self.client = client

    def list_requests(self, params={}, headers={}):
        return self.client.request('post', '/listRequests', params=params, headers=headers)

    def request_lookup(self, params={}, headers={}):
        return self.client.request('post', '/requestLookup', params=params, headers=headers)
