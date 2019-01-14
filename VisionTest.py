from ovl import Color
from ovl import Vision
from ovl import Filters

ColorToTest= Color.Color(low=[0, 28, 138], high=[40, 255, 255])
v = Vision.Vision(camera_port='D:\Downloads\img.jpg', color=ColorToTest, filters=[Filters.circle_filter])
v.display_contours()

