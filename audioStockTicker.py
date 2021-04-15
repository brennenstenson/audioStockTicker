# https://pypi.org/project/pyttsx3/
# https://github.com/ranaroussi/yfinance

import pyttsx3
import yfinance as yf
import time
import math
import sys

if len(sys.argv) < 3:
    print('provide two arguments: stock quote (eg. GME), and refresh time in seconds')
    exit()

quote = sys.argv[1]
seconds = int(sys.argv[2])

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# remove the 'and' in the hundreds unit
def ttsFormat(price):
    if price<100: return price
    hundreds = math.floor(price/100)*100
    price = price - hundreds
    return '{} {}'.format(hundreds, round(price,2))
    
while True:
    stock = yf.Ticker(quote)
    price = float(stock.info.get('regularMarketPrice'))
    engine.say(ttsFormat(price))
    engine.runAndWait()
    time.sleep(seconds)
