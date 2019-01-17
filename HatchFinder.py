from TargetFinder import TargetFinder
from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from ovl_eshel.Code import Filters
import cv2



class HatchVisionProcessing(TargetFinder):

    def __init__(self, camera_port, robot_ip):
        super().__init__(camera_port)
        hatch_color = Color.Color(low=[21, 131, 124], high=[27, 255, 255])
        self.vision = Vision.Vision(camera_port=camera_port, color=hatch_color,
                                    filters=[Filters.area_filter, size_filter], parameters=[[200], []],
                                    directions_function=Directions.x_center_directions, target_amount=4,
                                    connection_dst=robot_ip, port='HatchDirection')

    def enable(self):
        self.vision.start(print_results=False)

    def disable(self):
        self.vision.stop()


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


def size_filter( contour_list):
    output = contour_list
    output.sort(key=lambda contour: cv2.contourArea(contour))
    return output[len(output) - 1::]

