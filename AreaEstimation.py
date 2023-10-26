import scipy.misc
from PIL import Image
import random

img = scipy.misc.read('img_name')
countPunjab = 0
countIndia = 0
count = 0

while(count<=100000):
    x=random.randint(0,2735) #width of india map
    y=random.randint(0,2480) #height of india map
    z=0
    if(img[x][y][z]==60):
        countIndia = countIndia + 1
        count = count + 1
    else:
        if(img[x][y][z]==80):
            countPunjab = countPunjab + 1
            count = count + 1
            
areaEstimated = (countPunjab/countIndia) * 328763  #area of india
print(areaEstimated," km")