import requests
import json
url = "https://api.binance.com"
uri = '/api/v3/ticker/24hr'

querystring = {"symbol":"BTCBUSD"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url+uri, headers=headers, params=querystring)
print(response)
print(response.text)
data = json.loads(response.text)

# print(response.text)
print('lastPrice : {}'.format(data['lastPrice']))
# print('BTC Price : {}'.format(data[0]['trade_price']))
