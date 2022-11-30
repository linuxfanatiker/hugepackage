
import copy
from PIL import Image, ImageEnhance
import numpy as np
import pickle
from matplotlib import pyplot as plt
def pixelspas( im, new_item, yellow):
    for pixel in im.getdata():
        if (19<pixel[0]<90  and pixel[1]>50 and 50<pixel[2]):  # (np.all(pixel >lower_yellow) ) and 25<pixel[1] and 50<pixel[2]
            yellow = yellow + 1
            new_item.append((0, 100, 100))
        else:
            new_item.append(pixel)

    im.putdata(new_item)
    #print(yellow)
    plt.subplot(121)
    plt.imshow(img), plt.axis("off")
    plt.subplot(122)
    plt.imshow(im), plt.axis("off")
    plt.show()
    yellow = yellow/(600*800)
    return yellow

yellow = 0
new_item = []
ellow = []

img = Image.open('C:\\Test\\95.png')
im = copy.deepcopy(img).convert('HSV')
ellow.append(pixelspas(im, new_item, yellow))
print(ellow)


#im= im.convert('P', palette=Image.ADAPTIVE, colors=3)#.convert('RGB')