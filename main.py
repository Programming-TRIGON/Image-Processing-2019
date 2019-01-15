from networktables import NetworkTables
from VisionManager import VisionManager
import logging
import time
from CargoFinder import CargoFinder

ROBOT_IP = '127.0.0.1'

logging.basicConfig(level=logging.DEBUG)
targetFinders = {
    'cargo': CargoFinder(0)
}

try:
    visionManager = VisionManager(targetFinders)
    NetworkTables.initialize(server=ROBOT_IP)

    sd = NetworkTables.getTable("ImageProcessing")
    sd.addEntryListener(visionManager.targetChanged, immediateNotify=True)

    while True:
        time.sleep(1)
        # print(sd.getNumber('robotTime', 999))


finally:
    pass
    # visionManager.end()



