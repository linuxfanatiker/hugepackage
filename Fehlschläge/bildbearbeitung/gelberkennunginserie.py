
import copy
from PIL import Image, ImageEnhance
import numpy as np
import os
from matplotlib import pyplot as plt
def pixelspas( im, new_item, yellow):
    saturation=20
    value=50
    min_angle=30
    max_angle=70
    for pixel in im.getdata():
        if (min_angle<pixel[0]<max_angle and pixel[1]>saturation and value<pixel[2]):  # (np.all(pixel >lower_yellow) ) and 25<pixel[1] and 50<pixel[2]
            yellow = yellow + 1
            new_item.append((0, 255, 255))
        else:
            new_item.append(pixel)
    showme(new_item,im,img)
    yellow = yellow/(600*800)
    return yellow
def showme(new_item,im,img):
    im.putdata(new_item)
    plt.subplot(121)
    plt.imshow(img), plt.axis("off")
    plt.subplot(122)
    plt.imshow(im), plt.axis("off")
    plt.show()

yellow = 0
new_item = []
ellow = []
for i in range(156,167):
    img = Image.open("../../hugepackage-master2/hugepackage-master/hugepackage-Complete/package_testdaten/2022.11.29_testdaten_rev1/"+str(i)+".png")
    im = copy.deepcopy(img).convert('HSV')
    ellow.append(pixelspas(im, new_item, yellow))
    new_item.clear()
    #print(ellow)
    print(str(i)+".png")