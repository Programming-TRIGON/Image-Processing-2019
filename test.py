from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Filters
import cv2

CAMERA_PORT = 0

some_color = Color.Color(low=[0, 28, 138], high=[40, 255, 255])

v = Vision.Vision(camera_port=1, color=some_color)

conts, img = v.apply_sample(camera_port=1)
print('found {} contours'.format(len(conts)))
cv2.imshow('',img)
v.display_contours(img)
cv2.waitKey()
