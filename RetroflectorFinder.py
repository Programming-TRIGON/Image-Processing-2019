from TargetFinder import TargetFinder
from ovl_eshel.Code import Vision
from ovl_eshel.Code import Filters
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from Constants import RetroflectorConstants
from itertools import permutations
import cv2

class RetroflectorFinder(TargetFinder):

    def __init__(self, camera_port, robot_ip):
        super().__init__(camera_port)
        self.vision = Vision.Vision(camera_port=camera_port, color=Color.BuiltInColors.red_hsv,
                                    filters=[Filters.area_filter, self.reflector_filter],
                                    parameters=[[500], []],
                                    directions_function=Directions.x_center_directions,
                                    connection_dst=robot_ip, port='ImageProcessing')

    def reflector_filter(self, contours):
        rotated, _ = Filters.rotated_rectangle_filter(contours, RetroflectorConstants.rotated_rec_min_ratio)
        rotated.sort(key=lambda cont: cv2.minAreaRect(cont)[0][0])

        return rotated

    def enable(self):
        self.vision.start(print_results=False)

    def disable(self):
        self.vision.stop()