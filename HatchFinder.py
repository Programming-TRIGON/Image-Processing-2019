from TargetFinder import TargetFinder
from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from ovl_eshel.Code import Filters
from cv2 import convexHull
from cv2 import contourArea


class HatchVisionProcessing(TargetFinder):

    def __init__(self, camera_port, robot_ip):
        super().__init__(camera_port)
        hatch_color = Color.Color(low=[18, 87, 82], high=[47, 255, 255])
        self.vision = Vision.Vision(camera_port=camera_port, color=hatch_color,
                                    filters=[Filters.area_filter, size_filter],
                                    parameters=[[200], []],
                                    directions_function=Directions.xy_center_directions, target_amount=1,
                                    connection_dst=robot_ip, port='HatchDirection')

    def enable(self):
        self.vision.start(print_results=False)

    def disable(self):
        self.vision.stop()


def solidity_filter(contour_list, solidity):
    output = []
    for contour in contour_list:
        area = contourArea(contour)
        hull = convexHull(contour)
        solid = 100 * area / contourArea(hull)
        if (solid < solidity[0] or solid > solidity[1]):
            continue
        output.append(contour)
    return output


def size_filter(contour_list):
    output = contour_list
    output.sort(key=lambda contour: contourArea(contour))
    return output[len(output) - 1::]



