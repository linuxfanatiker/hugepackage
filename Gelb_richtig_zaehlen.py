# importing libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading the image data from desired directory
img = cv2.imread("0.jpg")
#cv2.imshow("0.jpg", img)
lower_yellow=np.array([0,104,104])
upper_yellow=np.array([224,255,255])

image_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask=cv2.inRange(image_hsv, lower_yellow, upper_yellow)
# counting the number of pixels
number_of_yellow_pix0 = np.sum(mask)/255
print('Number of yellow pixels:', number_of_yellow_pix0)
plt.subplot(121)
plt.imshow(img),plt.axis("off")
plt.subplot(122)
plt.imshow(mask),plt.axis("off")
plt.show()