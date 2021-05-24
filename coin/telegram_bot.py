import telegram
import time
import coin_api as c


def coin():
    a = c.get()
    btc_price = a['data']['XRP']['quote']['KRW']['price']
    return btc_price

TELEGRAM_TOKEN='1823266093:AAHZIcp3QSVx0cjdyKLAyuRwyWk2Z9KNhKw'
TELEGRAM_CHAT_ID = 159774767

TELEGRAM_TOKEN_2='1860043124:AAHGj6eFUWoMQXY1TYOG6-imhGH8HRNXB9E'
TELEGRAM_CHAT_ID_2 = 1816449388


telegram_bot = telegram.Bot(token=TELEGRAM_TOKEN)
telegram_bot_2 = telegram.Bot(token=TELEGRAM_TOKEN_2)

def send_message(message):
    telegram_bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=message)
    telegram_bot_2.sendMessage(chat_id=TELEGRAM_CHAT_ID_2, text=message)


if __name__ == '__main__':
    a = 1
    val_list = []
    while True:
        a += 1
        # print(a)
        btc_price = coin()
        btc_price = int(btc_price)
        print(btc_price)
        message = 'XRP = {price:,} (김프포함시 {price2:,}'.format(price=btc_price, price2=int(btc_price*1.115)) 
        send_message(message)
        if len(val_list) < 12:
            val_list.append(int(btc_price))
        else:
            val_list.pop(0)
            val_list.append(int(btc_price))
        heavy_drop = False
        drop_ratio = 1
        '''
        조건
        1. 1시간 이내에 최소 10% 이상 떨어짐.
        2. 
        '''
        for val in val_list:
            if btc_price/val <= 0.9:
                if drop_ratio > btc_price/val:
                    drop_ratio = btc_price/val
                    before_btc_price = val
                    heavy_drop = True

        
        if heavy_drop:
            message = '''
            현재 1시간 이내에 10% 이상 급등락한 국면입니다. {}원 대비 현재 {}입니다. 
            급등락한 비율은 {}% 입니다.'''.format(before_btc_price, btc_price, drop_ratio*100)
            send_message(message)
            print(message)
        # if a == 10:
        #     break
        time.sleep(300)