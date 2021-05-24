 #This example uses Python 2.7 and the python-request library.

import json

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# -------------------------------------------------------------------------------------

def get():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'symbol':'XRP',
    'convert':'KRW'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '3e5d5d33-1c6b-44d4-8469-8ec054cb04c3',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        # print(data)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        

if __name__ == '__main__':
    get()