
class ReflectorConstants:

    rotated_rec_min_ratio = 0.8


class CameraConstants:

    __name_format = '/dev/v4l/by-path/platform-3f980000.usb-usb-0:1.{}:1.0-video-index0'

    port_matrix = {'top_left': __name_format.format(2),
                   'top_right': __name_format.format(4),
                   'bottom_left': __name_format.format(5),
                   'bottom_right': __name_format.format(3)
                   }



