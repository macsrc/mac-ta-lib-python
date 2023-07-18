# imports
import pandas as pd
import pandas_datareader.data as pdr
import datetime
import talib
from talib.abstract import *
from talib import MA_Type

# print(AROON)

# print(AROON.info)


aapl = pd.read_csv('SBIN.csv')
aapl.plot()