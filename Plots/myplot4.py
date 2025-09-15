from numpy import *
from pylab import *
x=linspace(-5,5,100)
plot(x,4*(x*x))
plot(x,2*x+3)
legend(['Parabola','Equation Line'])
show()