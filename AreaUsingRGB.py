from PIL import Image
import random

im = Image.open('img_name')
rgb = im.convert('RGB')
countPunjab = 0
countIndia = 0
count = 0
while(count<=100000):
    x = random.randint(0,2375)
    y = random.randint(0,2480)
    z = 0
    r,g,b = rgb.getpixel((x,y))
    if(r==60):
        countIndia = countIndia + 1
        count = count + 1
    else:
        if(r==80):
            countPunjab = countPunjab + 1
            count = count + 1
            
estimatedArea = (countPunjab/countIndia) * 3287263
print(estimatedArea,' km')