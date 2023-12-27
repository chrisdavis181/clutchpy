class Campaigns:
    def __init__(self, client):
        self.client = client

    def render_template(self, params={}, headers={}):
        return self.client.request('post', '/renderTemplate', params=params, headers=headers)

    def trigger_custom_campaigns(self, params={}, headers={}):
        return self.client.request('post', '/triggerCustomCampaigns', params=params, headers=headers)
