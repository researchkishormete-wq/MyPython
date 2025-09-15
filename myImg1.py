from numpy import *
from pylab import *
img = plt.imread('Python.png')
print(img.shape)
img1=img[::2,::4]
print(img1.shape)
#imshow(img)
#imshow(img, cmap='gray')
#savefig('cosine.png')
#imshow(img[75:225,75:225])
#imshow(img[::4,::4])
#show()
