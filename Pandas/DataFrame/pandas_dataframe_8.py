# Using the previous DataFrame, we will delete a column
# using del function
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
   'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print (df)
print()

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print (df)
print()

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print (df)
