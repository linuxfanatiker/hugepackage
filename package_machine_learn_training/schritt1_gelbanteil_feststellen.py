## Gelb Anteil Feststellen
## Revision 1
## 1.12.2022

import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
import glob
import sys
import os
from natsort import natsorted

sorted_filelist = []

output_filename = sys.argv[1]

for file in sys.argv[2:]:
    sorted_filelist.append(os.path.basename(file))

path_to_files = os.path.dirname(sys.argv[2])
sorted_filelist = natsorted(sorted_filelist)


#quit()

def yellow_pixel_counter(original_bild, markiertes_bild):
    yellow_pixel=0
    original_bild=original_bild.convert('HSV')
    for pixel in original_bild.getdata():
        if (19<pixel[0]<90 and pixel[1]>5 and 50<pixel[2]):  # (np.all(pixel >lower_yellow) ) and 25<pixel[1] and 50<pixel[2]
            yellow_pixel += 1
            markiertes_bild.append((0, 255, 255))
        else:
            markiertes_bild.append(pixel)
    yellow_pixel /= (600*800)
    return yellow_pixel

#	---------------------------------------------

#	Hier könnte eine eigene Funktion enstehen
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


bilder_gelb_anteil = []

#runs=201
#path = "../package_testdaten/2022.11.30_testdaten_rev2"

for file in sorted_filelist:
    print ("Verarbeite Bild " + path_to_files+"/"+file)
    markiertes_bild = []
    aktuelles_bild = Image.open(path_to_files+"/"+file)
    bilder_gelb_anteil.append(yellow_pixel_counter(aktuelles_bild, markiertes_bild))


plt.plot(range(0,len(sorted_filelist)),bilder_gelb_anteil)
plt.show()


outfile=open(output_filename, 'w')
for cur_image in bilder_gelb_anteil:
    print(str(cur_image))
    outfile.write(str(cur_image)+"\n")

outfile.close()

