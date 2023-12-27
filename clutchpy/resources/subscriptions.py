class Subscriptions:
    def __init__(self, client):
        self.client = client

    def list_value_types(self, params={}, headers={}):
        return self.client.request('post', '/listValueTypes', params=params, headers=headers)

    def list_subscription_lists(self, params={}, headers={}):
        return self.client.request('post', '/listSubscriptionLists', params=params, headers=headers)
