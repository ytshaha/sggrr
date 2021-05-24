from django.shortcuts import render
import coin.coin_api as c
import coin.telegram_bot as telbot

bot = telegram.Bot(token='1823266093:AAHZIcp3QSVx0cjdyKLAyuRwyWk2Z9KNhKw')
chat_id = 159774767

# Create your views here.
def coin(request):
    a = c.get()
    btc_price = a['data'][0]['quote']['USD']['price']
    return render(request, 'coin/coin.html', {'btc_price':btc_price})



# -*- coding: utf-8 -*-

# import json
# import requests

# COIN_API_URL = 'https://pro-api.coinmarketcap.com/'

# API_KEY = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'
# API_SECRET = 'sandbox-api.coinmarketcap.com'


