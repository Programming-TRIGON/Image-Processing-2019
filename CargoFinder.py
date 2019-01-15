from TargetFinder import TargetFinder
from ovl import Vision
from ovl import Color
from ovl import Directions


class CargoFinder(TargetFinder):
    cargo_hsv = Color.Color(low=[0, 103, 83], high=[56, 255, 255])

    def __init__(self, camera_port):
        self.vision = Vision.Vision(camera_port=camera_port, color=Color.BuiltInColors.red_hsv,
                                    directions_function=self.custom_direction)

    def enable(self):
        self.vision.start()

    def disable(self):
        self.vision.frame_loop()

    def custom_direction(self, contours, target_amount, *args):
        Directions.x_center_directions(contours, target_amount)
