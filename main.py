from networktables import NetworkTables
from VisionManager import VisionManager
import logging
import time

ROBOT_IP = '127.0.0.1'

logging.basicConfig(level=logging.DEBUG)

try:
    visionManager = VisionManager()
    NetworkTables.initialize(server=ROBOT_IP)

    sd = NetworkTables.getTable("SmartDashboard")
    sd.addEntryListener(visionManager.targetChanged, immediateNotify=True)

    while True:
        time.sleep(1)
        print(sd.getNumber('robotTime', 999))


finally:
    pass
    # visionManager.end()



