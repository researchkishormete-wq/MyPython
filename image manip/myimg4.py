from pylab import *
import numpy as np
img = imread('Squares.png')
print(img)
print(img.shape)
img1 = img[75:225, 75:225]
#filt = arange(1,151).reshape(150,1)
filt=np.random.rand(150,150)
img1=img1.dot(filt)
imshow(img1)
show()
