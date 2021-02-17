# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 01:24:13 2021

@author: susmoy
"""

import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print(df)

"""
sum():- add rows
"""
print('\nPrint 1:\n', df.sum(), sep='')

"""
sum(1):- add columns
"""
print('\nPrint 1:\n', df.sum(1), sep='')

"""
mean(): 
"""
print('\nPrint 2:\nReturns the average value\n', df.mean(), sep='')

"""
std():
"""
print('\nReturns the Bressel standard deviation of the numerical columns\n', df.std(), sep='')

"""
describe(): Summarizing Data
"""
print('\nThe describe() function computes a summary of statistics pertaining to the DataFrame columns.\n')
print(df.describe())