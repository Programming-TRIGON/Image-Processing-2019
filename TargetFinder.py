from subprocess import call

class TargetFinder:
    """
    Each specific target finder class extends TargetFinder
    """
    def __init__(self, camera_port):
        self.camera_port = camera_port

    def enable(self):raise NotImplementedError("implement me in child class!")

    def disable(self):raise NotImplementedError("implement me in child class!")

    @staticmethod
    def set_exposure(self, camera, exposure):
        call(['v4l2-ctl', '-d', camera, '-c', 'exposure_auto=1',
              '-c', 'exposure_absolute={}'.format(exposure)])
