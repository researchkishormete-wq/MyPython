from numpy import *
from pylab import *
import array as arr
# Program to
A=array([1,2,3,4,5])
C=array([[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]])
A=arange(1,6)
C=arange(1,26).reshape(5,5)
A[2]=-3
C[2]=[3,4,-40,5,6]
C[-1]=[0,0,0,0,0]
print(A[0:3])
print(C[0:5:2,0:5:2])