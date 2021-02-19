# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000,
         62316, 64928, 67317, 68748, 73572]

# plot for normal developer
#plt.plot(ages_x, dev_y, 'k--', label='All Devs')
plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 
            70000, 71496, 75370, 83640]

# plot for python developer
plt.plot(ages_x, py_dev_y, color='b', marker='o', label='Python Devs')
# label the x axis
plt.xlabel('Ages')
# label the y axis
plt.ylabel('Median Salary (USD)')
# Set title for the plot
plt.title('Median Salary (USD) by age')

# add lagend for more information
plt.legend()

plt.show()