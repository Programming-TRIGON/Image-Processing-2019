from cv2 import *

#__name_format = 
#'/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.{}:1.0-video-index0'
#cam = cv2.VideoCapture(__name_format.format(4))
cam = cv2.VideoCapture(0)
s, img = cam.read()
if s:    # frame captured without any errors
    imwrite("Image.jpg", img)  # save image
else:
	print('uh oh')
