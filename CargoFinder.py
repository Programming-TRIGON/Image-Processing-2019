from TargetFinder import TargetFinder
from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from ovl_eshel.Code import Filters


class CargoFinder(TargetFinder):
    cargo_hsv = Color.Color(low=[0, 0, 215], high=[40, 255, 255])
    test_color = Color.Color(low=[0, 69, 149], high=[45, 209, 255])

    def __init__(self, camera_port, robot_ip):
        super().__init__(camera_port)
        self.vision = Vision.Vision(camera_port=camera_port, color=Color.BuiltInColors.red_hsv,
                                    filters=[Filters.area_filter, Filters.circle_filter],
                                    parameters=[[300], [0.6]],
                                    directions_function=Directions.xy_center_directions, target_amount=1,
                                    connection_dst=robot_ip, port='CargoDirection')

    def enable(self):
        self.vision.start(print_results=False)

    def disable(self):
        self.vision.stop()
