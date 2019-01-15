from threading import Thread


class VisionManager:
    visionThread = Thread()

    def __init__(self, targets):
        """
        Args:
            targets: dictionary of keys and targetFinder classes
        """
        self.targetDict = targets

    def targetChanged(self, table, key, value, isNew):
        """
        This method handles the thread running the processing. When the target is changed in the NT (presumably by the
        robot), this method will cancel the current :func:`TargetFinder  <TargetFinder.TargetFinder>`
        and run the new one.
        :param table:
        :type table:
        :param key:
        :type key:
        :param value:
        :type value:
        :param isNew:
        :type isNew:
        :return:
        :rtype:
        """
        if table == 'ip':
            if key == 'target':
                if value in self.targetDict:
                    self.targetFinder.disable()  # cancel current targetFinder
                    self.visionThread.join()

                    self.targetFinder = self.targetDict[value]
                else:
                    raise KeyError("target from nt does not exist!")

                self.visionThread = Thread(target=self.targetFinder.enable)
                self.visionThread.start()

    def end(self):
        self.targetFinder.disable()
        self.visionThread.join()
