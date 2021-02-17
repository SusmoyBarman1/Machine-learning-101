# -*- coding: utf-8 -*-

"""
Reindexing changes the row labels and column labels of a DataFrame. To reindex means to conform the data to match a given set of labels along a particular axis.

Multiple operations can be accomplished through indexing like −
    -Reorder the existing data to match a new set of labels.
    -Insert missing value (NA) markers in label locations where no data for the label existed.
"""
import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2021-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

print(df)

print('\nReindexing the dataframe\n')
df_reindex = df.reindex(index=[0, 2, 4, 6, 8, 10], columns=['A', 'C', 'B'])
print(df_reindex)

"""
Reindex to Align with Other Objects
You may wish to take an object and reindex its axes to be labeled the same as another object. Consider the following example to understand the same.
"""

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

print('\n', df1, sep='')
df3 = df1.reindex_like(df2)
print('\ndf3 reindex like df2\n')
print(df3)


print('\ndf4 reindex like df1, empty values will fill with last value\n')
print(df2.reindex_like(df1, method='ffill'))
print()
print(df2.reindex_like(df1, method='bfill'))
print()
print(df2.reindex_like(df1, method='nearest'))
print('\nData Frame with Forward Fill limiting to 1\n')
print(df2.reindex_like(df1, method='ffill', limit=1))