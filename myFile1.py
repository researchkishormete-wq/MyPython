from numpy import *
from pylab import *
# Program to
L=loadtxt("student_record.txt",usecols=(3,4,5,6,7), delimiter=";")
print(L)
print(L.shape)