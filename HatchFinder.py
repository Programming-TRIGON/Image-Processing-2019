from TargetFinder import TargetFinder
from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from ovl_eshel.Code import Filters
import cv2


class HatchVisionProcessing(TargetFinder):

    def __init__(self, camera_port):
        super().__init__(camera_port)
        hatch_color = Color.Color(low=[0, 28, 138], high=[40, 255, 255])
        self.vision = Vision.Vision(camera_port=camera_port, color=hatch_color,
                                    filters=[Filters.area_filter, self.solidity_filter], parameters=[[200], [0, 89]],
                                    directions_function=Directions.x_center_directions, )

    def solidity_filter(self, contour_list, solidity):
        output = []
        for contour in contour_list:
            area = cv2.contourArea(contour)
            hull = cv2.convexHull(contour)
            solid = 100 * area / cv2.contourArea(hull)
            if (solid < solidity[0] or solid > solidity[1]):
                continue
            output.append(contour)
        return output

    def enable(self):
        self.vision.start(print_results=False)

    def disable(self):
        self.vision.stop()

