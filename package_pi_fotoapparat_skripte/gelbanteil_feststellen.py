import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
import sys


def yellow_pixel_counter(im):
    yellow_pixel=0
    for pixel in im.getdata():
        if (19<pixel[0]<90  and pixel[1]>20 and 70<pixel[2]):  # (np.all(pixel >lower_yellow) ) and 25<pixel[1] and 50<pixel[2]
            yellow_pixel += 1
    yellow_pixel /= (600*800)
    return yellow_pixel

#   Das Bild soll als command line argument uebergeben werden
path = sys.argv[1]

#print ("Verarbeite Bild "+path)
img = Image.open(path)
img.convert('HSV')
gelb_anteil=yellow_pixel_counter(img)

#print("Der Gelbanteil betraegt "+str(gelb_anteil))
print(str(gelb_anteil))
