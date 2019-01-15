from dis import code_info

from ovl import Color
from ovl import Vision
from ovl import Filters
from TargetFinder import TargetFinder


class HatchVisionProcessing(TargetFinder):

    def __init__(self):
        HatchColor = Color.Color(low=[0, 28, 138], high=[40, 255, 255])
        self.v = Vision.Vision(camera_port=0, color=HatchColor, filters=[Filters.area_filter(min_area=200, max_area=3000), self.SolidityFileter], parameters=[[], [1,2]], )

    def solidityFileter(self, contour_list, solidity):


        return contour_list

    def enable(self):
        pass

    def  disable(self):
        pass