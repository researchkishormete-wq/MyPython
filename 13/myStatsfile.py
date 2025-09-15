from numpy import *
from pylab import *
from scipy import stats
# Program to store records in file
#Write a program to store total marks and percentages of all
#students in a file.
file=open("myfile.txt","w")
L=loadtxt("student_record.txt",usecols=(3,4,5,6,7), delimiter=";")
for record in L:
    totalmarks=sum(record)
    perc = mean(record)
    str1=str(totalmarks)+" "+str(perc) +"\n"
    file.write(str1)
file.close()
