from numpy import *
from pylab import *
from scipy import stats
# Program to sort all subject marks in desc order
L=loadtxt("student_record.txt",usecols=(3,4,5,6,7), delimiter=";")
s=array(L).reshape(len(L),5)
c=s[:,0]
print(sort(c)[::-1])
