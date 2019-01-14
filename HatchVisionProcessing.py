from ovl import Color
from ovl import Vision
from ovl import Filters
from TargetFinder import TargetFinder


class HatchVisionProcessing(TargetFinder):

    def __init__(self):
        HatchColor = Color.Color(low=[0, 28, 138], high=[40, 255, 255])
        self.v = Vision.Vision(camera_port=0, color=HatchColor, filters=[Filters.circle_filter, self.examplefileter], parameters=[[], [1,2]], )


    def enable(self):
        pass
    def examplefileter(self, contores, a,b):
        pass


