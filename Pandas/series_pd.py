import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
seriess = pd.Series(data)

print(seriess)

seriess = pd.Series(data, index=[100, 101, 102, 103])
print('\n',seriess, sep='')

data = {'a':0, 'b':2, 'c':4, 'd':6}
seriess = pd.Series(data)
print('\n',seriess, sep='')

data = {'a':0, 'b':2, 'c':4}
seriess = pd.Series(data, index=['b', 'c', 'd', 'a'])
print('\n',seriess, sep='')