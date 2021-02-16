##1
## Create a dataframe from list of dict
import pandas as pd

data = [{'a':2, 'b':3}, {'c':23, 'd':43}]
df = pd.DataFrame(data)
print(df)

## 2
data = {
        'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([5, 6, 7, 8], index=['b', 'a', 'c', 'd'])
       }

df = pd.DataFrame(data)
print('\n\n', df, sep='')

print('\nCreating new column in existing dataframe:')
df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(df)

print('\nCreating new column by adding two existing columns: ')
df['four'] = df['one'] + df['two']
print(df)


## Get all rows by indicating column name
print('\n', df.loc['b'], sep='')

## Get all rows by indicating index of column
print('\n', df.iloc[3], sep='')

## add two dataframe
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])

df1 = df1.append(df2)
print('\n---------\n', df1, sep='')

## Delete rows by indicating label
df1 = df1.drop(0)
print('\n', df1, sep='')