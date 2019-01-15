from threading import Thread

class VisionManager:
    visionThread = Thread()

    def __init__(self, targets):
        """

        :param targets: keys and targetFinder classes
        :type targets: Dictionary
        """
        self.targetDict = targets
        self.targetFinder = None

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
        print('val changed')
        print(table, key, value, isNew)
        if str(table) == 'NetworkTable: /ImageProcessing/':
            if key == 'target':
                if value in self.targetDict:
                    print('target is now {}'.format(value))
                    self.cancelTargetFinder()  # cancel current targetFinder

                    self.targetFinder = self.targetDict[value]
                else:
                    raise KeyError("target from nt does not exist!")

                self.visionThread = Thread(target=self.targetFinder.enable)
                self.visionThread.start()

    def end(self):
        self.cancelTargetFinder()

    def cancelTargetFinder(self):
        if self.targetFinder is not None:
            self.targetFinder.disable()
        if self.visionThread.is_alive():
            self.visionThread.join()
