from pylab import *
from PIL import *
import numpy as np
img = imread('pexels-photo-462118.jpeg')
print(img.shape)
img1=np.random.rand(333,500,3)
img1=img+img1 
imshow(img1)
show()