class TargetFinder:
    def __init__(self, camera_port):
        self.camera_port = camera_port

    def enable(self):raise NotImplementedError("implement me in child class!")

    def disable(self):raise NotImplementedError("implement me in child class!")