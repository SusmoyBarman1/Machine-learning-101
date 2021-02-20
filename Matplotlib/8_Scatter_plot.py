# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
#plt.scatter(x, y, c='green', marker='X')
plt.scatter(x, y, c='green', edgecolor='black', linewidth=1, alpha=0.75)

plt.show() 