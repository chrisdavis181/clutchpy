class Cards:
    def __init__(self, client):
       self.client = client

    def allocate_child_card(self, params={}, headers={}):
       return self.client.request('post', '/allocateChildCard', params=params, headers=headers)
    
    def allocate_card(self, params={}, headers={}):
       return self.client.request('post', '/allocate', params=params, headers=headers)
    
    def reactivate_card(self, params={}, headers={}):
       return self.client.request('post', '/reactivate', params=params, headers=headers)

    def update_card_balance(self, params={}, headers={}):
       return self.client.request('post', '/updateBalance', params=params, headers=headers)

    def update_card_account(self, params={}, headers={}):
       return self.client.request('post', '/updateAccount', params=params, headers=headers)

    def search(self, params={}, headers={}):
       return self.client.request('post', '/search', params=params, headers=headers)
