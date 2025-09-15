#Image as matrix, 2-D array
from pylab import *
img = imread('Squares.png')
img = imread('pexels-photo-462118.jpeg')
print(img)
print(img.shape)
img1 = img[75:225, 75:225]
imshow(img1)
show()
