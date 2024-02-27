import yfinance as yf
# aapl = yf.download('AAPL', '2019-1-1','2019-12-27')
# print(aapl)

# imports
import pandas as pd
import pandas_datareader.data as pdr
import talib as ta
import yfinance as yf
import csv

# from talib.abstract import *
# from talib import MA_Type
from datetime import datetime

# Get today's date in yyyy-mm-dd format
today_date = datetime.today().strftime('%Y%m%d')
# today_date = '20230728'

tickerStrings = ['SBIN.NS', 'MSFT']  # , 'MSFT'], GRASIM.NS, SBIN.NS
tickerfile = '';
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period="1y", interval="1d")
    data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
    data.to_csv(f'ticker_{ticker}_{today_date}.csv')  # ticker_AAPL_yyyymmss.csv for example
    tickerfile = 'ticker' + '_' + ticker + '_' + today_date + ".csv"
    #     print('ticker'+ '_' + ticker + '_' + today_date + ".csv")
    print(tickerfile)

aapl = pd.read_csv(tickerfile)
aapl
