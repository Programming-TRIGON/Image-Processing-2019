from TargetFinder import TargetFinder
from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from ovl_eshel.Code import Filters
from networktables import NetworkTables

class CargoFinder(TargetFinder):
    cargo_hsv = Color.Color(low=[0, 103, 83], high=[56, 255, 255])
    test_color = Color.Color(low=[0, 188, 130], high=[50, 255, 255])

    def __init__(self, camera_port, robot_ip):
        self.vision = Vision.Vision(camera_port=camera_port, color=Color.BuiltInColors.red_hsv,
                                    filters=[Filters.area_filter],
                                    parameters=[[2000, 68000]],
                                    directions_function=Directions.x_center_directions,
                                    connection_dst=robot_ip, port='ImageProcessing')


    def enable(self):
        self.vision.start()

    def disable(self):
        self.vision.frame_loop()

    def custom_direction(self, contours, target_amount, *args):
        print('so far so good')
        return Directions.x_center_directions(contours, target_amount)
