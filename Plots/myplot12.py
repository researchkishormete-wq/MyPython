from pylab import *

x_units = [1, 2, 3, 5]
y_units = [10, 24, 36, 48]

tick_label = ['one', 'two', 'three', 'five']
bar(x_units, y_units, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

xlabel('x - axis')
ylabel('y - axis')
title('My bar chart!')
show()