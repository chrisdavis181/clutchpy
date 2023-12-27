from client import Client
from resources.campaigns import Campaigns 
from resources.cards import Cards
from resources.coupons import Coupons 
from resources.events import Events 
from resources.requests import Requests
from resources.subscriptions import Subscriptions
from resources.transactions import Transactions

class ClutchPy(Client):
    def __init__(self, brand, location, terminal, key, secret, timeout, env):
        self.brand = brand
        self.location = location
        self.terminal = terminal
        self.key = key
        self.secret = secret
        self.timeout = timeout
        if env == 'prod':
            self.env = ''
        else:
            self.env = '-stage'
        
        self.base_url = f'https://api{self.env}.clutch.com/merchant'

        self.client = Client(
            base_url=self.base_url,
            key=self.key,
            secret=self.secret,
            location=self.location,
            terminal=self.terminal,
            brand=self.brand,
            timeout=self.timeout,
            env=self.env
        )

        self.campaigns = Campaigns(self.client)
        self.cards = Cards(self.client)
        self.coupons = Coupons(self.client)
        self.events = Events(self.client)
        self.requests = Requests(self.client)
        self.subscriptions = Subscriptions(self.client)
        self.transactions = Transactions(self.client)
