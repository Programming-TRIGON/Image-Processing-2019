from threading import Thread
import time

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
        print(table, key, value)
        if str(table) == 'NetworkTable: /ImageProcessing/':
            if key == 'target':
                if value in self.targetDict.keys():
                    print('target is now {}'.format(value))
                    self.cancelTargetFinder()  # cancel current targetFinder
                    # time.sleep(1)
                    self.targetFinder = self.targetDict[value]
                else:
                    print("{} target from nt does not exist!".format(value))

                self.visionThread = Thread(target=self.targetFinder.enable)
                self.visionThread.setName(self.targetDict[value])
                self.visionThread.start()

    def end(self):
        self.cancelTargetFinder()

    def cancelTargetFinder(self):
        if self.targetFinder is not None:
            self.targetFinder.disable()
            print(self.targetFinder.vision.is_running)
        if self.visionThread.is_alive():
            print('thread is alive')
            self.visionThread.join()
            print('thread joined')
