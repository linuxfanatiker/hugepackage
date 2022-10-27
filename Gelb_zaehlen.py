# importing libraries
import cv2
import numpy as np

# reading the image data from desired directory
img = cv2.imread("Yellow.png")
cv2.imshow('Image', img)
img = np.reshape(img,(2500,-1))

# counting the number of pixels
number_of_yellow_pix1 = np.sum(np.all(img == [204,255,255], axis=1))
number_of_yellow_pix2= np.sum(np.all(img == [153,255,255], axis=1))
number_of_yellow_pix3 = np.sum(np.all(img == [102,255,255], axis=1))
number_of_yellow_pix4 = np.sum(np.all(img == [51,255,255], axis=1))
number_of_yellow_pix= number_of_yellow_pix1+number_of_yellow_pix2+number_of_yellow_pix3+number_of_yellow_pix4
print('Number of yellow pixels:', number_of_yellow_pix)
