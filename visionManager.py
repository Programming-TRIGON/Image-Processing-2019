from threading import Thread

class VisionManager:
    visionThread = Thread()

    def __init__(self, targets):
        self.targetDict = targets

    def targetChanged(self, table, key, value, isNew):
        if table == 'ip':
            if key == 'target':
                self.visionThread.join()
                self.visionThread = Thread(target=self.targetDict[value].enable)