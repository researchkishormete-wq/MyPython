from numpy import *
from pylab import *
x,y=loadtxt("company-a-data.txt", unpack=True)
figure(1)
pie(y,labels=x)
title('Profit')
#savefig('cosine.png')
figure(2)
bar(x,y,fill=False,hatch='/')
show()
