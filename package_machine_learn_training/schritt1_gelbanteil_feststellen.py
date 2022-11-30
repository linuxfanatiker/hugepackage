import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt

def yellow_pixel_counter( im, new_item):
    yellow_pixel=0
    for pixel in im.getdata():
        if (19<pixel[0]<90  and pixel[1]>50 and 50<pixel[2]):  # (np.all(pixel >lower_yellow) ) and 25<pixel[1] and 50<pixel[2]
            yellow_pixel += 1
            new_item.append((0, 100, 100))
        else:
            new_item.append(pixel)

#	Plottet das Bild und daneben die Gelberkennung
#       ----------------------------------------------
    """
    im.putdata(new_item)
    print(yellow)
    plt.subplot(121)
    plt.imshow(img), plt.axis("off")
    plt.subplot(122)
    plt.imshow(im), plt.axis("off")
    plt.show()#"""
    yellow_pixel /= (600*800)
    return yellow_pixel
#	---------------------------------------------

new_item = []
bilder_gelb_anteil = []
runs=201
path = "../package_testdaten/2022.11.30_testdaten_rev2"

for i in range(0,runs):
    print ("Verarbeite Bild " + str(i) + "\n")
    img = Image.open(path + '/' + str(i) + '.png')
    bilder_gelb_anteil.append(yellow_pixel_counter(img, new_item))


plt.plot(range(0,runs),bilder_gelb_anteil)
plt.show()

for cur_image in bilder_gelb_anteil:
    print(str(cur_image))
