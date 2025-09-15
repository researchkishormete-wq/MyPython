from numpy import *
from pylab import *
m1=matrix([1,2,3,4])
l1=[1,2,3,4,5,6,7,8,9]
m2=asmatrix(l1).reshape(3,3)
print(m2)
m3=asmatrix(arange(0,9).reshape(3,3))
print(m3)
m4=m2*m3
print(inv(m2))