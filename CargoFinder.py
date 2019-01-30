from TargetFinder import TargetFinder
from ovl_eshel.Code import Vision
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from ovl_eshel.Code import Filters
from cv2 import contourArea


class CargoFinder(TargetFinder):
    def __init__(self, camera_port, robot_ip):
        super().__init__(camera_port)
        cargo_color = Color.Color(low=[0, 122, 83], high=[36, 255, 255])
        self.vision = Vision.Vision(camera_port=camera_port, color=cargo_color,
                                    filters=[Filters.area_filter, size_filter],
                                    parameters=[[300], []],
                                    directions_function=Directions.xy_center_directions, target_amount=1,
                                    connection_dst=robot_ip, port='CargoDirection')

    def enable(self):
        self.vision.start(print_results=False)

    def disable(self):
        self.vision.stop()


def size_filter(contour_list):
    output = contour_list
    output.sort(key=lambda contour: contourArea(contour))
    return output[len(output) - 1::]
