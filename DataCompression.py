import numpy as np
from PIL import Image

img = Image.open('img_name')
pixelMap = img.load()

I = np.asanyarray(Image.open('img_name'))
imgNew = Image.new(img.mode,img.size)
pixelNew = imgNew.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        
        if(pixelMap[i,j]>=0 and pixelMap[i,j]<=31):
            pixelMap[i,j] = 0
            
        elif(pixelMap[i,j]>=32 and pixelMap[i,j]<=63):
            pixelMap[i,j] = 1
            
        elif(pixelMap[i,j]>=64 and pixelMap[i,j]<=95):
            pixelMap[i,j] = 2
            
        elif(pixelMap[i,j]>=96 and pixelMap[i,j]<=127):
            pixelMap[i,j] = 2
            
img2 = pixelMap.load()
img.save('new_image_name')

