# ClutchPy

## Endpoint Grouping/Scope
Link to API Documentation: https://apidocs.clutch.com/

### Card Operations
| Method            | Docs                                                             |
| :---------------- | :------                                                          |
| allocateChildCard | https://apidocs.clutch.com/?javascript#child-cards               |
| allocate          | https://apidocs.clutch.com/?javascript#allocatin-cards           |
| reactivate        | https://apidocs.clutch.com/?javascript#reactivating-cards        |
| updateAccount     | https://apidocs.clutch.com/?javascript#updating-card-information |
| updateBalance     | https://apidocs.clutch.com/?javascript#updating-balances         |
| search            | https://apidocs.clutch.com/?javascript#searching-cards           |

### Transactions and History
| Method            | Docs                                                        |
| :---------------- | :------                                                     |
| cardHistory       | https://apidocs.clutch.com/?javascript#card-history-lookup  |
| voidTransaction   | https://apidocs.clutch.com/?javascript#voiding-transactions |
| returnMerchandise | https://apidocs.clutch.com/?javascript#returns              |
| checkout          | https://apidocs.clutch.com/?javascript#checkouts            |
| transfer          | https://apidocs.clutch.com/?javascript#transfer             |

### Coupon Operations
| Method         | Docs                                               |
| :------------- | :------                                            |
| allocateCoupon | https://apidocs.clutch.com/?javascript#allocating-coupons  |
| couponDetails  | https://apidocs.clutch.com/?javascript#coupon-interactions |

### Event Handling
| Method          | Docs                                                        |
| :-------------- | :------                                                     |
| createEventType | https://apidocs.clutch.com/?javascript#managing-event-types |
| listEventTypes  | https://apidocs.clutch.com/?javascript#managing-event-types |

### Requests and Lookup
| Method        | Docs                                                    |
| :------------ | :------                                                 |
| listRequests  | https://apidocs.clutch.com/?javascript#listing-requests |
| requestLookup | https://apidocs.clutch.com/?javascript#listing-requests |

### Value and Subscription Lists
| Method                | Docs                                                              |
| :-------------------- | :------                                                           |
| listValueTypes        | https://apidocs.clutch.com/?javascript#listing-value-types        |
| listSubscriptionLists | https://apidocs.clutch.com/?javascript#listing-subscription-lists |

### Template and Campaign Handling
| Method                 | Docs                                             |
| :--------------------- | :------                                          |
| renderTemplate         | https://apidocs.clutch.com/?javascript#structure |
| triggerCustomCampaigns | https://apidocs.clutch.com/?javascript#triggers  |

## Installation
```
$ pip install clutchpy
```

Note: This python module has not been publish to the PyPI (Python Package Index) yet so this installation command will not work yet.

## Usage
```python
import clutchpy

# initialize the clutch api client
client = ClutchAPI(
  brand='YOUR BRAND', 
  location='YOUR LOCATION', 
  terminal='YOUR TERMINAL', 
  key='YOUR PRIVATE KEY', 
  secret='YOUR PRIVATE SECRET', 
  timeout='YOUR DESIRED DEFAULT TIMEOUT', 
  env='stage' # valid environment values are 'stage' and 'prod'
)

# define search parameters
params = {'filters': {}}

# send a search request
client.cards.search(params)
```
