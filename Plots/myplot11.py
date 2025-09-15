from pylab import *

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]

scatter(x, y, label="stars", color="green",
            marker="1", s=30)

xlabel('x - axis')
ylabel('y - axis')

title('Scatter plot')
legend()
show()