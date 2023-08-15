import yfinance as yf
import requests_cache
from datetime import timedelta


# more info about yfinance: https://github.com/ranaroussi/yfinance/wiki

#session to cache the info
#experation is after 1 hours
session = requests_cache.CachedSession('yfinance.cache', expire_after=timedelta(hours=1))

# name of the user-agent
session.headers['User-agent'] = 'TradeSupport/1.0'


msft = yf.Ticker('MSFT', session = session)

#get all stock info 
msft.info
print(msft.info['currentPrice'])
print(msft.info['totalCash'])