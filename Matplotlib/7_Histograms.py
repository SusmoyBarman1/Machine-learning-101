# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#ages = [18, 19, 21, 25, 25, 26, 26, 30, 32, 38, 45, 55, 55]
#bins = [10, 20, 30, 40, 50, 60]
#plt.hist(ages, bins=bins, edgecolor='black')

data = pd.read_csv('hist_data.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90]
plt.hist(ages, bins=bins, edgecolor='black')