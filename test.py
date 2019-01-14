from ovl import Vision
from ovl import Color
from ovl import Filters
import cv2

CAMERA_PORT = 0

some_color = Color.Color(low=[0, 28, 138], high=[40, 255, 255])

v = Vision.Vision(camera_port=r'D:\Downloads\img.jpg', color=some_color, filters=[Filters.area_filter(), ])

conts, img = v.apply_sample(camera_port='D:\Downloads\img.jpg')
print('found {} contours'.format(len(conts)))
cv2.imshow('', img)
cv2.waitKey()
v.display_contours(img)



