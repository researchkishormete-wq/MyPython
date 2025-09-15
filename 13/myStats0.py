# Program to find total and percentage of each student
from numpy import *
from pylab import *
from scipy import stats
L=loadtxt("student_record.txt",usecols=(3,4,5,6,7), delimiter=";")
for record in L:
    totalmarks=sum(record)
    perc = mean(record)
    print(totalmarks, " ", perc)
