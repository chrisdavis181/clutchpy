class Transactions: 
    def __init__(self, client):
        self.client = client

    def void_transaction(self, params={}, headers={}):
        return self.client.request('post', '/voidTransaction', params=params, headers=headers)

    def return_merchandise(self, params={}, headers={}):
        return self.client.request('post', '/returnMerchandise', params=params, headers=headers)

    def create_checkout(self, params={}, headers={}):
        return self.client.request('post', '/checkout', params=params, headers=headers)
    
    def transfer(self, params={}, headers={}):
        return self.client.request('post', '/transfer', params=params, headers=headers)

    def get_card_history(self, params={}, headers={}):
        return self.client.request('post', '/cardHistory', params=params, headers=headers)
