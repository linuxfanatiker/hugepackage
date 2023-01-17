import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
import sys

sys.path.append('../libraries')
from gelberkennung import yellow_features

#   Das Bild soll als command line argument uebergeben werden
path = sys.argv[1]

#print ("Verarbeite Bild "+path)
img = Image.open(path)
#img = img.convert('HSV')
gelb_anteil, laengste_reihe, reihen_ueber_max, reihen_unter_max=yellow_features(img)

#print("Gelbanteil, Lage der Reihe mit den meisten gelben Pixeln, gelbe Reihen darueber, und darunter")
print(str(gelb_anteil)+','+str(laengste_reihe)+','+str(reihen_ueber_max)+','+str(reihen_unter_max))
