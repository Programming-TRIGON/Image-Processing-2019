from TargetFinder import TargetFinder
from ovl_eshel.Code import Vision
from ovl_eshel.Code import Filters
from ovl_eshel.Code import Color
from ovl_eshel.Code import Directions
from subprocess import call
from cv2 import contourArea
from cv2 import minAreaRect


class ReflectorFinder(TargetFinder):

    def __init__(self, camera_port, robot_ip):
        super().__init__(camera_port)
        reflector_color = Color.Color(low=[44, 64, 128], high=[83, 255, 255])
        self.vision = Vision.Vision(camera_port=camera_port, color=reflector_color,
                                    filters=[Filters.area_filter, size_filter],
                                    parameters=[[20], []],
                                    directions_function=Directions.xy_center_directions, target_amount=1,
                                    connection_dst=robot_ip, port='ReflectorDirection')

    def enable(self):
        self.vision.start(print_results=False)

    def disable(self):
        self.vision.stop()

    def set_exposure(self, exposure):
        call(['v4l2-ctl', self.camera_port, '-c',
              'exposure_auto=1', '-c', 'exposure_absolute={}'.format(safe_format(exposure))])


def safe_format(x):
    if x is None:
        return 0
    return x


def size_filter(contour_list):
    output = contour_list
    output.sort(key=lambda contour: contourArea(contour))
    return output[len(output) - 2::]


def reflector_filter(self, rotated_contour):
    rotated_contour.sort(key=lambda cont: minAreaRect(cont)[0][0])
    results = []

    # find reflectors by pairs - each pair has one positive and one negatively angled reflector
    for i in range(0, len(rotated_contour) - 1):
        left = rotated_contour[i]
        right = rotated_contour[i + 1]

        left_angle = minAreaRect(left)[2]
        right_angle = minAreaRect(right)[2]
        if left_angle > 0 and right_angle < 0:
            results.append((left, right))

    return results
