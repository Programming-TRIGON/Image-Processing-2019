from ovl import Vision
from ovl import Color
from ovl import Filters
import cv2


color_cargo_hsv = Color.Color(low=[0, 122, 50], high=[34, 255, 255])
v = Vision.Vision(camera_port=1, color=color_cargo_hsv)


