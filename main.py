from networktables import NetworkTables
from VisionManager import VisionManager
import logging
import time
from ovl_eshel.Code import Color
from CargoFinder import CargoFinder
# from RetroflectorFinder import RetroflectorFinder
from HatchFinder import HatchVisionProcessing
from Constants import CameraConstants

ROBOT_IP = '10.59.90.2'

logging.basicConfig(level=logging.DEBUG)

targetFinders = {
    # 'cargo': CargoFinder(CameraConstants.port_matrix['bottom_right'], ROBOT_IP),
    # 'retro': RetroflectorFinder(0, ROBOT_IP),
    # 'hatch': HatchVisionProcessing(CameraConstants.port_matrix['bottom_left'], ROBOT_IP)
    'cargo': Color.Color(low=[18, 87, 82], high=[47, 255, 255]),
    'hatch': Color.Color(low=[0, 115, 107], high=[25, 255, 255])
    # Bag: 'cargo' and 'hatch' cant get the same camera because the program trying to open the same camera twice!
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



