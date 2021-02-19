from matplotlib import pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')

ages_x = [18, 19, 20, 21, 22]
x_indexes = np.arange(len(ages_x))
width = 0.25
py_dev_y = [20046, 17100, 20000, 24744, 30500]
# plot for python developer
plt.bar(x_indexes, py_dev_y, width=width, label='Python Devs')

dev_y = [17784, 16500, 18012, 20628, 25206]
# plot for normal developer
plt.bar(x_indexes + width, dev_y, width=width, label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by age')
plt.xticks(ticks=x_indexes, labels=ages_x)
plt.legend()
plt.show()

