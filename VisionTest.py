from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from ovl_eshel.Code import Filters
import cv2

ColorToTest = Color.Color(low=[0, 28, 138], high=[40, 255, 255])
v = Vision.Vision(camera_port='D:\Downloads\img.jpg', color=ColorToTest, filters=[Filters.area_filter], parameters=[[200]], directions_function=Directions.x_center_directions, target_amount=4,)
conts, img = v.apply_sample(camera_port='D:\Downloads\img.jpg')
print('found {} contours'.format(len(conts)))
cv2.imshow('', img)
cv2.waitKey()
v.display_contours(img)
