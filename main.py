from ovl import Vision
from ovl import Color
from ovl import Filters
import cv2

CAMERA_PORT = 0

color_cargo_hsv = Color.Color(low=[0, 103, 83], high=[56, 255, 255])
v = Vision.Vision(camera_port=CAMERA_PORT, color=color_cargo_hsv)

conts, img = v.apply_sample(camera_port=CAMERA_PORT)
print 'found {} contours'.format(len(conts))
cv2.imshow('', img)
cv2.waitKey()
v.display_contours(img)



