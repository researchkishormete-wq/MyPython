from numpy import *
from pylab import *
x=linspace(1,20,20)
figure(1)
loglog(x,5*(x**3))
title('Log Log')
#savefig('cosine.png')
show()
