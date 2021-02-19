# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
#plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')
plt.xkcd()

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

# plot for normal developer
#plt.plot(ages_x, dev_y, 'k--', label='All Devs')
plt.plot(ages_x, dev_y, label='All Devs')

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

# plot for python developer
plt.plot(ages_x, py_dev_y, label='Python Devs')

# label the x axis
plt.xlabel('Ages')
# label the y axis
plt.ylabel('Median Salary (USD)')
# Set title for the plot
plt.title('Median Salary (USD) by age')

# add lagend for more information
plt.legend()
#plt.grid(True)

# save the plot
#plt.savefig('plot.png')

plt.show()