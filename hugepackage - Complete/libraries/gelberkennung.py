import copy
from matplotlib import pyplot as plt



def yellow_features(img):
    # Aufloesung feststellen    
    width, height = img.size

    yellow_pixel_amount=0
    yellow_pixel_largest_row=0
    yellow_pixel_per_row=[0]*height

    # Schritt 1: Bild in HSV konvertieren
    img = img.convert('HSV')

    # Schritt 2: Durch alle Pixel des Bilds durchlaufen
    current_pixel_number=0
    for pixel in img.getdata():
        current_row = int(current_pixel_number/width)                   # Aktuelle Reihe im Bild feststellen
        if (19<pixel[0]<90 and pixel[1]>5 and 50<pixel[2]):             # Dies erkennt das Gelb
            yellow_pixel_amount += 1                                    # Anzahl der gelben Pixel erhoehen
            yellow_pixel_per_row[current_row] +=1                       # Anzahl der gelben Pixel in der entsprechenden Reihe erhoehen
        current_pixel_number += 1

    # Schritt 3: Reihe mit den meisten gelben Pixel herausfinden
    for current_row in range(0, len(yellow_pixel_per_row)):
        if (yellow_pixel_per_row[current_row]>yellow_pixel_per_row[yellow_pixel_largest_row]):
            yellow_pixel_largest_row=current_row                        # Diese Reihe beinhaltet das größte Vorkommen gelber Pixel. Merken.

    yellow_pixel_amount_normed = yellow_pixel_amount / (width*height)
    yellow_pixel_largest_row_normed = yellow_pixel_largest_row / height

    return [yellow_pixel_amount_normed, yellow_pixel_largest_row_normed]

def plot_img_with_yellow_pixels(img):
    # Aufloesung feststellen    
    width, height = img.size

    leuchtend_rot_hsv = (0, 255, 255)
    leuchtend_gruen_hsv = (90, 255, 255)

    yellow_pixel_amount=0
    yellow_pixel_largest_row=0
    yellow_pixel_per_row=[0]*height

    # Schritt 1: Bild in HSV konvertieren
    img_orig = img.convert('HSV')
    img_copy = copy.deepcopy(img)
    img_copy = img_copy.convert('HSV')
    img_rot_data = []

    # Schritt 2: Durch alle Pixel des Bilds durchlaufen
    current_pixel_number=0
    for pixel in img_orig.getdata():
        current_row = int(current_pixel_number/width)                   # Aktuelle Reihe im Bild feststellen
        if (19<pixel[0]<90 and pixel[1]>5 and 50<pixel[2]):             # Dies erkennt das Gelb
            img_rot_data.append(leuchtend_rot_hsv)
            yellow_pixel_per_row[current_row] +=1                       # Anzahl der gelben Pixel in der entsprechenden Reihe erhoehen
        else:
            img_rot_data.append(pixel)                                       # Pixelweises kopieren in das neue Bild
        current_pixel_number += 1

    # Schritt 3: Reihe mit den meisten gelben Pixel herausfinden
    for current_row in range(0, len(yellow_pixel_per_row)):
        if (yellow_pixel_per_row[current_row]>yellow_pixel_per_row[yellow_pixel_largest_row]):
            yellow_pixel_largest_row=current_row                        # Diese Reihe beinhaltet das größte Vorkommen gelber Pixel. Merken.

    for pixel in range(0,width):
        img_rot_data[(yellow_pixel_largest_row*width)+pixel]=leuchtend_gruen_hsv  # Die Reihe mit dem größten Vorkommen komplett grün machen

    img_copy.putdata(img_rot_data)

    # Schritt 4: Plotten
    plt.subplot(121)
    plt.imshow(img_orig), plt.axis("off")
    plt.subplot(122)
    plt.imshow(img_copy), plt.axis("off")
    plt.show()

