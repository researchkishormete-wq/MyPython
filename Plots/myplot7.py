from numpy import *
from pylab import *
x = ['Maths', 'Physics', 'Chemistry']
y1 = [95, 88, 45]
plot(x, y1, label="Ram")
y2 = [67, 45, 56]
plot(x, y2, label="Sham")
y3 = [28, 67, 90]
plot(x, y3, label="Mohan")
xlabel('Subjects')
ylabel('Marks')
title('Three lines on same graph!')
legend()
show()