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
                                    filters=[Filters.area_filter,
                                             Filters.rotated_rectangle_filter,
                                             self.reflector_filter],
                                    parameters=[[500],
                                                [RetroflectorConstants.rotated_rec_min_ratio], []],
                                    directions_function=,
                                    connection_dst=robot_ip, port='ImageProcessing')

    def reflector_filter(self, rotated):
        rotated.sort(key=lambda cont: cv2.minAreaRect(cont)[0][0])
        results = []

        # 
        for i in range(0, len(rotated) - 1):
            left = rotated[i]
            right = rotated[i + 1]

            left_angle = cv2.minAreaRect(left)[2]
            right_angle = cv2.minAreaRect(right)[2]
            if left_angle > 0 and right_angle < 0:
                results.append((left, right))

        return results

    def

    def enable(self):
        self.vision.start(print_results=False)

    def disable(self):
        self.vision.stop()
