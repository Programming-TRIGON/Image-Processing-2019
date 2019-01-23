from networktables import NetworkTables
from VisionManager import VisionManager
import logging
import time
from CargoFinder import CargoFinder
# from RetroflectorFinder import RetroflectorFinder
from HatchFinder import HatchVisionProcessing
from Constants import CameraConstants

ROBOT_IP = '10.59.90.2'

logging.basicConfig(level=logging.DEBUG)

targetFinders = {
    'cargo': CargoFinder(CameraConstants.port_matrix['bottom_right'], ROBOT_IP),
    # 'retro': RetroflectorFinder(0, ROBOT_IP),
    'hatch': HatchVisionProcessing(CameraConstants.port_matrix['bottom_left'], ROBOT_IP)
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



