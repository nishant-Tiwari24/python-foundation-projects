import numpy as np
from PIL import Image
width = 5
height = 4
array = np.zeros([width,height,3],dtype=np.uint8)
img = Image.fromarray(array)
img.save('test.png')
array1 = np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100] = [255,128,0]
img = Image.fromarray(array1)
img.save('test1.png')

#to get rgb values of a image
image1 = Image.open('test1.png')
rgb = image1.convert('RGB')
r,g,b = rgb.getpixel(1,1)
print(r,g,b)
