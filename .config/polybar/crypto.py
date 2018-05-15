#!/usr/bin/env python3

import json
import requests


r = requests.get('https://api.coinmarketcap.com/v1/ticker/burst/')
burst_usd = json.loads(r.text)[0]["price_usd"]
r = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
bitcoin_usd = json.loads(r.text)[0]["price_usd"]

status_message = "BURST: ${burst}   BTC: ${bitcoin}".format(
        burst = burst_usd
        , bitcoin = bitcoin_usd
        )

print(status_message)
