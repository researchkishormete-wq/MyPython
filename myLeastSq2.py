from numpy import *
from pylab import *
L,t=loadtxt("pendulum.txt", unpack=True)
tsq=t*t
inter_mat=array((1,ones_like(1)))
print(inter_mat)
A=inter_mat.T
result = lstsq(A, tsq,rcond=-1)
m,c=result[0]
tsq_fit=m*L+c
figure(1)
plot(L,tsq,'bo')
plot(L,tsq_fit,'r')
title('Least Square Fit')
"""
T^2=m*L+c
"""
#savefig('cosine.png')
show()
