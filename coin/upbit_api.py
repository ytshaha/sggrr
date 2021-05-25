import requests
import json
url = "https://api.upbit.com/v1/ticker"

querystring = {"markets":"KRW-BTC"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

# print(response.text)
print(data)
print('BTC Price : {}'.format(data[0]['trade_price']))
