from threading import Thread

class VisionManager:
    visionThread = Thread()

    def __init__(self, targets):
        """
        :param targets: dictionary of keys and targetFinder classes
        """
        self.targetDict = targets

    def targetChanged(self, table, key, value, isNew):
        if table == 'ip':
            if key == 'target':
                if value in self.targetDict:
                    targetFinder = self.targetDict[value]
                else:
                    raise KeyError("target from nt does not exist!")

                targetFinder.disable()
                self.visionThread.join()
                self.visionThread = Thread(target=targetFinder.enable)
                self.visionThread.start()

    def end(self):
        self.visionThread.join()
