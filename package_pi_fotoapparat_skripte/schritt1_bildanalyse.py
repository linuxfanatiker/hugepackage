## Gelb Anteil Feststellen
## Revision 2
## 2.12.2022
## Letzte Aenderung: Lage der Line mit den meisten gelben Pixeln

import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
import glob
import sys
import os
from natsort import natsorted
sys.path.append("../libraries")
from gelberkennung import yellow_features

sorted_filelist = []
output_filename = sys.argv[1]

for file in sys.argv[2:]:
    sorted_filelist.append(os.path.basename(file))

path_to_files = os.path.dirname(sys.argv[2])
sorted_filelist = natsorted(sorted_filelist)

bilder_gelb_anteil = []
bilder_laengste_reihe = []

for file in sorted_filelist:
    print ("Verarbeite Bild " + path_to_files+"/"+file)
    aktuelles_bild = Image.open(path_to_files+"/"+file)
    analyse = yellow_features(aktuelles_bild)
    bilder_gelb_anteil.append(analyse[0])
    bilder_laengste_reihe.append(analyse[1])

plt.plot(range(0,len(sorted_filelist)),bilder_gelb_anteil)
plt.show()

outfile=open(output_filename, 'w')
for i in range(0, len(bilder_gelb_anteil)):
    ausgabe = str(bilder_gelb_anteil[i])+","+str(bilder_laengste_reihe[i])
    print(ausgabe)
    outfile.write(ausgabe+"\n")
    i += 1

outfile.close()

