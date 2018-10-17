import pandas as pd
import quandl

#taking all row and colomn to the data frame.
df = quandl.get('WIKI/GOOGL')

#taking only open,high,low,close and volume to the data frame
df = df[['Adj. Open', 'Adj. High','Adj. Low', 'Adj. Close', 'Adj. Volume']]

#daily parcent change
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

#taking only the usefull columns
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())
