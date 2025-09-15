from numpy import *
from pylab import *
from scipy import stats
# Program to store records in List
rec=[]
L=loadtxt("student_record.txt",usecols=(3,4,5,6,7), delimiter=";")
for record in L:
    totalmarks=sum(record)
    perc = mean(record)
    rec.append([totalmarks, perc])
print(rec)