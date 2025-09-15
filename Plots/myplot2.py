from numpy import *
from pylab import *
x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
y=[0.69,0.9,1.19,1.30,1.47,1.58,1.77,1.83,1.94]
ysquare = square(y)
plot(x,ysquare)
xlabel(r"$x$")
ylabel(r"$y$")
show()


#plot(x,ysquare,'o')
