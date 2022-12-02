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

sorted_filelist = []

output_filename = sys.argv[1]

for file in sys.argv[2:]:
    sorted_filelist.append(os.path.basename(file))

path_to_files = os.path.dirname(sys.argv[2])
sorted_filelist = natsorted(sorted_filelist)


#quit()

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
    #print("gelb verteilung")
    #print(yellow_per_row)
    #print("Längste Linie")
    #print(max_yellow)
    #print("Reihe")
    #print(max_row_number)

    max_row_number /= 600
    ergebnis = [yellow_pixel, max_row_number]
    return ergebnis

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
bilder_laengste_reihe = []

#runs=201
#path = "../package_testdaten/2022.11.30_testdaten_rev2"

for file in sorted_filelist:
    print ("Verarbeite Bild " + path_to_files+"/"+file)
    markiertes_bild = []
    aktuelles_bild = Image.open(path_to_files+"/"+file)
    aktuelles_bild = aktuelles_bild.convert('HSV')
    analyse = yellow_pixel_counter(aktuelles_bild)
    bilder_gelb_anteil.append(analyse[0])
    bilder_laengste_reihe.append(analyse[1])


plt.plot(range(0,len(sorted_filelist)),bilder_gelb_anteil)
plt.show()


outfile=open(output_filename, 'w')
for i in range(0, len(bilder_gelb_anteil)):
#for cur_image in bilder_gelb_anteil:
    ausgabe = str(bilder_gelb_anteil[i])+","+str(bilder_laengste_reihe[i])
    print(ausgabe)
    outfile.write(ausgabe+"\n")
    i += 1

outfile.close()

