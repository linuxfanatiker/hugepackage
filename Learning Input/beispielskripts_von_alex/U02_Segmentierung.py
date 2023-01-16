import matplotlib.pyplot as plt
import skimage.segmentation as seg
import skimage.color as color
from skimage import io
from time import sleep
from picamera import PiCamera

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

def segmentation_start(filename_input, filename_gray, filename_color, camera):
	camera.capture(filename_input)
	sleep(1)
	print('Roh-Image Gespeichert %s' % filename_input)

	image = io.imread(filename_input)
	image_felzenszwalb = seg.felzenszwalb(image)
	io.imsave(filename_gray,image_felzenszwalb)
	image_felzenszwalb_colored = color.label2rgb(image_felzenszwalb, image, kind='avg')
	io.imsave(filename_color,image_felzenszwalb_colored)


camera=PiCamera()
for i in range(0,10):
	filename_input=str(i)+'_input.jpg'
	filename_gray=str(i)+'_gray.jpg'
	filename_color=str(i)+'_color.jpg'
	segmentation_start(filename_input, filename_gray, filename_color, camera)
