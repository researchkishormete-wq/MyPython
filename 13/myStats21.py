from numpy import *
from pylab import *
from scipy import stats
# Program to
L=loadtxt("student_record.txt",usecols=(4,5), delimiter=";")
totalmarks=sum(L[0])
print(median(L[0]))
print(mean(L[0]))
#print(stats.mode(L[0]))