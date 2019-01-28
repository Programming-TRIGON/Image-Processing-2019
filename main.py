from networktables import NetworkTables
from VisionManager import VisionManager
import logging
import time
from CargoFinder import CargoFinder
from ReflectorFinder import ReflectorFinder
from HatchFinder import HatchFinder
from Constants import CameraConstants

ROBOT_IP = '10.59.90.2'

logging.basicConfig(level=logging.DEBUG)

targetFinders = {
    'cargo': CargoFinder(CameraConstants.port_matrix['bottom_right'], ROBOT_IP),
    'hatch': HatchFinder(CameraConstants.port_matrix['bottom_right'], ROBOT_IP),
    'reflector': ReflectorFinder(CameraConstants.port_matrix['top_right'], ROBOT_IP)
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



