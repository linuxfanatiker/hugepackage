from time import sleep
from picamera import PiCamera


camera = PiCamera()
# camera.start_preview()
for i in range(0,10):
    #timestamp = time.time()
    filename= 'img'+str(i)+'.jpg' #+str(timestamp)
    camera.capture(filename)
    sleep(1)
    print('Captured %s' % filename)
