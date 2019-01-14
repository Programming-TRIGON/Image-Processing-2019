from threading import Thread

class VisionManager:
    visionThread = Thread()

    def __init__(self, targets):
        self.targetDict = targets

    def targetChanged(self, table, key, value, isNew):
        if table == 'ip':
            if key == 'target':
                if value in self.targetDict:
                    targetFinder = self.targetDict[value]
                else:
                    raise("target from sd does not exist!")

                targetFinder.disable()
                self.visionThread.join()
                self.visionThread = Thread(target=targetFinder.enable)
                self.visionThread.start()
                