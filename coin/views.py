from django.shortcuts import render
import coin.coin_api as c
import coin.telegram_bot as telbot

# Create your views here.
def coin(request):
    a = c.get()
    btc_price = a['data']['XRP']['quote']['KRW']['price']
    return render(request, 'coin/coin.html', {'btc_price':btc_price})

def coin2(request):
    return render(request, 'coin/coin2.html', {})

# -*- coding: utf-8 -*-

# import json
# import requests

# COIN_API_URL = 'https://pro-api.coinmarketcap.com/'

# API_KEY = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'
# API_SECRET = 'sandbox-api.coinmarketcap.com'


