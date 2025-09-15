from numpy import *
from pylab import *
a=asmatrix(arange(1,17).reshape(4,4))
a[0,1]=0
a[1,3]=0
ai=inv(a)
#print(ai)
print(norm((ai),ord=inf))