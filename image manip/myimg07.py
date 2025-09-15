from PIL import Image
from pylab import *
def addimg(): 
    try: 
        #Relative Path 
        #Image on which we want to paste 
        img = Image.open("pexels-photo-462118.jpeg")  
                #transposing image  
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT) 
        imshow(transposed_img)
        show()
    except IOError: 
        pass
  
addimg()

##An additional argument for an optional image mask image is also available. 
