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
sys.path.append("../../libraries")
from gelberkennung import yellow_features

sorted_filelist = []
output_filename = sys.argv[1]

for file in sys.argv[2:]:
    sorted_filelist.append(os.path.basename(file))

path_to_files = os.path.dirname(sys.argv[2])
sorted_filelist = natsorted(sorted_filelist)

bilder_gelb_anteil = []
bilder_laengste_reihe = []
bilder_gelb_ueber_max = []
bilder_gelb_unter_max = []
debug_ueber_unter_verh = []

for file in sorted_filelist:
    print ("Verarbeite Bild " + path_to_files+"/"+file)
    aktuelles_bild = Image.open(path_to_files+"/"+file)
    analyse = yellow_features(aktuelles_bild)
    bilder_gelb_anteil.append(analyse[0])
    bilder_laengste_reihe.append(analyse[1])
    bilder_gelb_ueber_max.append(analyse[2])
    bilder_gelb_unter_max.append(analyse[3])
    if (analyse[3]>0):
       debug_ueber_unter_verh.append(analyse[2]/analyse[3])
    else:
       debug_ueber_unter_verh.append(0)

figure, axis = plt.subplots(4,1)

axis[0].plot(range(0,len(sorted_filelist)),bilder_gelb_anteil, color='black')
axis[1].plot(range(0,len(sorted_filelist)),bilder_gelb_ueber_max, color='red')
axis[2].plot(range(0,len(sorted_filelist)),bilder_gelb_unter_max, color='blue')
axis[3].plot(range(0,len(sorted_filelist)),debug_ueber_unter_verh, color='cyan')
axis[3].set_ylim([0,1.1])
plt.show()

outfile=open(output_filename, 'w')
for i in range(0, len(bilder_gelb_anteil)):
    ausgabe = str(bilder_gelb_anteil[i])+","+str(bilder_laengste_reihe[i])+","+str(bilder_gelb_ueber_max[i])+","+str(bilder_gelb_unter_max[i])
    print(ausgabe)
    outfile.write(ausgabe+"\n")
    i += 1

outfile.close()

