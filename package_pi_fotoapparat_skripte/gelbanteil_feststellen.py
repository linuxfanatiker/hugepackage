import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
import sys

sys.path.append('../libraries')
from gelberkennung import yellow_features

#def yellow_pixel_counter(im):
#    yellow_pixel=0
#    for pixel in im.getdata():
#        if (19<pixel[0]<90 and pixel[1]>5 and 50<pixel[2]):  # (np.all(pixel >lower_yellow) ) and 25<pixel[1] and 50<pixel[2]
#            yellow_pixel += 1
#    yellow_pixel /= (600*800)
#    return yellow_pixel


#   Das Bild soll als command line argument uebergeben werden
path = sys.argv[1]

#print ("Verarbeite Bild "+path)
img = Image.open(path)
#img = img.convert('HSV')
gelb_anteil, laengste_reihe=yellow_features(img)

#print("Der Gelbanteil betraegt "+str(gelb_anteil))
print(str(gelb_anteil)+','+str(laengste_reihe))
