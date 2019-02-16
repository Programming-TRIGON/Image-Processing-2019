from networktables import NetworkTables
from VisionManager import VisionManager
import logging
import time
from CargoFinder import CargoFinder
from ReflectorFinder import ReflectorFinder
from HatchFinder import HatchFinder
from Constants import CameraConstants
from subprocess import call


ROBOT_IP = '10.59.90.2'
EXPOSURE = 0


logging.basicConfig(level=logging.DEBUG)

targetFinders = {
    'cargo': CargoFinder(CameraConstants.port_matrix['bottom_right'], ROBOT_IP),
    'hatch': HatchFinder(CameraConstants.port_matrix['bottom_right'], ROBOT_IP),
    'reflector': ReflectorFinder(CameraConstants.port_matrix['top_right'], ROBOT_IP)

}


def safe_format(x):
    if x is None:
        return 0
    return x


try:
    visionManager = VisionManager(targetFinders)
    NetworkTables.initialize(server=ROBOT_IP)
    sd = NetworkTables.getTable("ImageProcessing")
    sd.addEntryListener(visionManager.targetChanged, immediateNotify=True)

    call(['v4l2-ctl', '-d', CameraConstants.port_matrix['top_right'], '-c', 'exposure_auto=1',
          '-c', 'exposure_absolute={}'.format(safe_format(EXPOSURE))])


    lastThread = ''
    while True:
        # Find out which VisionTracker is running in the vision thread (to make sure the threads were ending... ):
        # lastThread = visionManager.visionThread.getName()
        # if visionManager.visionThread.getName() != lastThread:
        #     print(visionManager.visionThread.getName())
        time.sleep(1000000) # This while loop wont interfere the vision code EVER!

finally:
    visionManager = VisionManager(targetFinders)
    visionManager.end()



