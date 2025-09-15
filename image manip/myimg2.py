#Convert image to Gray-Scale
from pylab import *
img = imread('Squares.png')
imshow(img, cmap='gray')
show()