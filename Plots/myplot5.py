from numpy import *
from pylab import *
x,y=loadtxt("pendulum.txt", unpack=True)
plot(x,y, color='green', linestyle='dashed')
title('Graph of Pendulum')
xlabel('x - axis')
ylabel('y - axis') 
show()