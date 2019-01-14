from ovl import Vision
from ovl import Color
from ovl import Filters
import cv2

CAMERA_PORT = 1

color_cargo_hsv = Color.Color(low=[0, 122, 50], high=[34, 255, 255])
v = Vision.Vision(camera_port=CAMERA_PORT, color=color_cargo_hsv)

cam = cv2.VideoCapture(CAMERA_PORT)
_, img = cam.read()
cam.release()

v.get_contours(img=img)
v.apply_filter(filter_function=Filters.circle_filter)
v.display_contours(img=img)
