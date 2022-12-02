import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
import sys

sys.path.append('../libraries')
from gelberkennung import yellow_features
from gelberkennung import plot_img_with_yellow_pixels

#   Das Bild soll als command line argument uebergeben werden
path = sys.argv[1]

img = Image.open(path)
plot_img_with_yellow_pixels(img)

