from TargetFinder import TargetFinder
from ovl import Vision
from ovl import Color
from ovl import Directions
from ovl import Filters
from networktables import NetworkTables

class CargoFinder(TargetFinder):
    cargo_hsv = Color.Color(low=[0, 103, 83], high=[56, 255, 255])
    test_color = Color.Color(low=[147, 92, 46], high=[179, 255, 168])

    def __init__(self, camera_port, robot_ip):
        self.vision = Vision.Vision(camera_port=camera_port, color=Color.BuiltInColors.red_hsv,
                                    filters=[Filters.area_filter],
                                    parameters=[[2000, 68000]],
                                    directions_function=self.custom_direction)

        self.vision.connection_address = robot_ip
        self.vision.connection_type = 'NT'
        self.vision.network_port = 'vision_results'
        NetworkTables.initialize(server=robot_ip)
        self.vision.socket = NetworkTables.getTable('ImageProcessing')

    def enable(self):
        self.vision.start()

    def disable(self):
        self.vision.frame_loop()

    def custom_direction(self, contours, target_amount, *args):
        return Directions.x_center_directions(contours, target_amount)
