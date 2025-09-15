from numpy import *
from pylab import *
img = imread('Python.png')
#imshow(img)
#imshow(img, cmap='gray')
#savefig('cosine.png')
#imshow(img[75:225,75:225])
imshow(img[:,:,0])
show()
