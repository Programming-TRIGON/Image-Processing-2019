from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Filters
import cv2
from HatchFinder import HatchVisionProcessing
import time


def size_filter(contour_list):
    output = contour_list
    output.sort(key=lambda contour: cv2.contourArea(contour))
    return output[len(output) - 1::]


def solidity_filter(contour_list, solidity):
    output = []
    for contour in contour_list:

        area = cv2.contourArea(contour)
        hull = cv2.convexHull(contour)
        solid = 100 * area / cv2.contourArea(hull)
        if (solid < solidity[0] or solid > solidity[1]):
            continue
        output.append(contour)
    return output


CAMERA_PORT = 1
ROBOT_IP = '127.0.0.1'

# hatch_finder = HatchVisionProcessing(CAMERA_PORT, ROBOT_IP)
# hatch_finder.enable()
# time.sleep(20)
# hatch_finder.disable()
some_color = Color.Color(low=[10, 48, 0], high=[29, 255, 170])
some_color2 = Color.Color(low=[10, 165, 149], high=[19, 255, 255])
#
v = Vision.Vision(camera_port=1, color=some_color,
                  filters=[Filters.area_filter], parameters=[[]], connection_dst=ROBOT_IP)
#
conts, img = v.apply_sample(camera_port=1)
print('found {} contours'.format(len(conts)))
v.display_contours(img)
cv2.waitKey()
