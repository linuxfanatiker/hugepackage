import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
import sys


def yellow_pixel_counter(im):
    yellow_pixel=0
    yellow_per_row=[0]*600
    i=0
    max_row_number=0
    max_yellow=0
    for pixel in im.getdata():
        if (19<pixel[0]<90  and pixel[1]>5 and 50<pixel[2]):  # (np.all(pixel >lower_yellow) ) and 25<pixel[1] and 50<pixel[2]
            yellow_pixel += 1
            yellow_per_row[int(i/800)] +=1
        i+=1
    yellow_pixel /= (600*800)
    i=0
    for row in yellow_per_row:
        if(row>max_yellow):
            max_yellow=row
            max_row_number=i
        i+=1
    print("gelb verteilung")
    print(yellow_per_row)
    print("Längste Linie")
    print(max_yellow)
    print("Reihe")
    print(max_row_number)
    return yellow_pixel

#   Das Bild soll als command line argument uebergeben werden
#path = sys.argv[1]

#print ("Verarbeite Bild "+path)
img = Image.open('C:\\Users\\m4xr0\\Documents\\GitHub\\hugepackage\\package_testdaten\\2022.11.30_testdaten_rev2\\0.png')
img =img.convert('HSV')
gelb_anteil=yellow_pixel_counter(img)

#print("Der Gelbanteil betraegt "+str(gelb_anteil))
print(str(gelb_anteil))
