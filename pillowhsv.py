
import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
def pixelspas( im):
    yellow = 0
    new_item = []
    for pixel in im.getdata():
        if(19 < pixel[0] < 90 and pixel[1] > 5 and 50 < pixel[2]):  # (np.all(pixel >lower_yellow) ) and 25<pixel[1] and 50<pixel[2]
            yellow += 1
            new_item.append((0, 255, 255))
        else:
            new_item.append(pixel)
    im.putdata(new_item)
    plt.subplot(121)
    plt.imshow(img), plt.axis("off")
    plt.subplot(122)
    plt.imshow(im), plt.axis("off")
    plt.show()
    yellow /=(600*800)

   # print("rueckgabe der pixelspas "+str(yellow))
    return yellow

yellow = 0
new_item = []
ellow = []
runs=201
#"""

for i in range(0,runs):
    #img = Image.open('C:\\Test\\'+ str(i) + '.png') #C:\Users\m4xr0\Documents\GitHub\hugepackage\package_testdaten\2022.11.30_testdaten_rev2
    img = Image.open('C:\\Users\\m4xr0\\Documents\\GitHub\\hugepackage\\package_testdaten\\2022.11.30_testdaten_rev2\\' + str(i) + '.png')
    im = copy.deepcopy(img).convert('HSV')
    ellow.append(pixelspas(im))
    print(ellow[i],str(i))

plt.plot(range(0,runs),ellow)
plt.show()

outfile =open("dataarray", 'wb')
pickle.dump(ellow,outfile)
outfile.close()
"""
img = Image.open('C:\\Test\\95.png')
im = copy.deepcopy(img).convert('HSV')
ellow.append(pixelspas(im, new_item, yellow))
print(ellow)

"""
#im= im.convert('P', palette=Image.ADAPTIVE, colors=3)#.convert('RGB')