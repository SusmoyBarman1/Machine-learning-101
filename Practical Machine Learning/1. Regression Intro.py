import pandas as pd
import quandl
import math

#taking all row and colomn to the data frame.
df = quandl.get('WIKI/GOOGL')

#taking only open,high,low,close and volume to the data frame
df = df[['Adj. Open', 'Adj. High','Adj. Low', 'Adj. Close', 'Adj. Volume']]

#daily parcent change
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

#taking only the usefull columns
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'

#filling the missing values with a lower number, because we can not work with the missing values in machine learning
df.fillna(-99999, inplace=True)

#predict the data for next 10 days by ceiling 0.1
forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

print(df.head())
