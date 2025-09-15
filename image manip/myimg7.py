from PIL import Image
from pylab import *
def addimg(): 
    try: 
        #Relative Path 
        #Image on which we want to paste 
        img = Image.open("pexels-photo-462118.jpeg")  
          
        #Relative Path 
        #Image which we want to paste 
        img2 = Image.open("pexels-photo-443446.jpeg")  
        img.paste(img2, (50, 50)) 
          
        #Saved in the same relative location 
        img.save("pasted_picture.jpg") 
        imshow(img)
        show()
    except IOError: 
        pass
  
addimg()

##An additional argument for an optional image mask image is also available. 
