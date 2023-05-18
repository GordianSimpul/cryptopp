#!/bin/env python3

import requests


CMC_API_KEY = 'd75c930e-a436-4149-a3ce-78440bf6a968'
CMCQuote="https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol=%s" 
curr = "USD"
headers_dict = {'X-CMC_PRO_API_KEY' : "%s" % CMC_API_KEY}
coin = "BTSG,SHD"
cmcq_r = requests.get(CMCQuote % coin, headers=headers_dict)
cmcqJSON = cmcq_r.json()
#print(cmcqJSON)

for c in coin.split(','):
    print(float(cmcqJSON['data'][c.upper()][0]['quote'][curr]['price']))

