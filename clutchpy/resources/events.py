class Events:
    def __init__(self, client):
        self.client = client

    def create_event_type(self, params={}, headers={}):
        return self.client.request('post', '/createEventType', params=params, headers=headers)

    def list_event_types(self, params={}, headers={}):
        return self.client.request('post', '/listEventTypes', params=params, headers=headers)
