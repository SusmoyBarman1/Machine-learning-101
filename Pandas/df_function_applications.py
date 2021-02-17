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
                   [0, 0, 0]], 
                   columns=['col1', 'col2', 'col3'])
print(df)
print('\nAdd 10 with every element\n')
print(df.pipe(adder, 10))
#print('\n',df, sep='')