from numpy import *
from pylab import *
from scipy import stats
# Program to
L=loadtxt("student_record.txt",usecols=(3,4,5,6,7), delimiter=";")
print(L)
#totalmarks=sum(L[0,:])
s=array(L).reshape(len(L),5)
s=sort(L)
#print(s)

print("Median ", median(L[0]))
print("Mean ", mean(L[0]))
#print(stats.mode(L[0]))