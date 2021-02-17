# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:29:27 2021

@author: susmoy
"""

import pandas as pd
import numpy as np

def adder(ele1, ele2):
    return ele1 + ele2

df = pd.DataFrame([[1, 2, 3],
                   [11, 22, 33],
                   [0, 0, 0],
                   [-1, -1, -1]], 
                   index = ['row1', 'row2', 'row3', 'row4'],
                   columns=['col1', 'col2', 'col3'])
print(df)
print('\nAdd 10 with every element\n')
print(df.pipe(adder, 10))


print('\nApply columns wise:\n')
print(df.apply(lambda x: x.max() - x.min()))

print('\nApply mean() columns wise:\n')
print(df.apply(np.mean))


print('\nApply mean() row wise:\n')
print(df.apply(np.mean, axis=1))

print('\nApply specific function in every element:\n')
print(df.applymap(lambda x: x**2))