
import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt

infile =open("dataarray", 'rb')
new_array=pickle.load(infile)#, encoding='bytes'

print(new_array)
#im= im.convert('P', palette=Image.ADAPTIVE, colors=3)#.convert('RGB')