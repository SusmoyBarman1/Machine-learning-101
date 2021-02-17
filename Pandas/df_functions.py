# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:42:52 2021

@author: susmoy
"""

import pandas as pd
import numpy as np

d = {'name': pd.Series(['Tom', 'James', 'Ricky', 'vin', 'steve', 'smith', 'jack']),
     'age': pd.Series([25, 26, 25, 23, 30, 29, 23]), 
     'Rating': pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])
     }

df = pd.DataFrame(d)

"""	
T: Transposes rows and columns.
"""
print('Print 1:', df, '\nTranspose:', df.T, sep='\n')

"""
axes: Returns a list with the row axis labels and column axis labels as the only members.
"""
print('\nPrint 2\nRow axis labels and column axis labels are:', df.axes, sep='\n')


"""
dtypes: Returns the dtypes in this object.
"""
print('\nprint 3:\nTypes of the values:', df.dtypes, sep='\n')

"""
empty: True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
"""
print('\nprint 4:\nIs the dataframe empty?', df.empty, sep='\n')

"""
ndim: Number of axes / array dimensions.
"""
print('\nprint 5:\nNumber of dimention of dataframe', df.ndim, sep='\n')


"""	
shape: Returns a tuple representing the dimensionality of the DataFrame.
"""
print('\nprint 6:\nShape of dataframe', df.shape, sep='\n')


"""
size: Number of elements in the NDFrame.
"""
print('\nPrint 7:\nThe total number of elements in our object is:', df.size, sep='\n')

"""
values: Numpy representation of NDFrame.
"""
print ("\nPrint 8:\nThe actual data in our data frame is:", df.values, sep='\n')

"""
head(): Returns the first n rows.
"""
print ("\nPrint 9:\nThe first 3 rows of the data frame is", df.head(3), sep='\n')

"""
tail(): Returns last n rows.
"""
print ("\nPrint 10:\nThe last 3 rows of the data frame is", df.tail(3), sep='\n')