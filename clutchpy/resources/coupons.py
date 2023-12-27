class Coupons:
    def __init__(self, client):
        self.client = client
    
    def get_coupon_details(self, params={}, headers={}):
        return self.client.request('post', '/couponDetails', params=params, headers=headers)
    
    def allocate_coupon(self, params={}, headers={}):
        return self.client.request('post', '/allocateCoupon', params=params, headers=headers)
