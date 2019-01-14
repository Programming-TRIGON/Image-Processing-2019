from networktables import NetworkTables
from VisionManager import VisionManager
import logging
import time

ROBOT_IP = '10.59.90.2'

logging.basicConfig(level=logging.DEBUG)

try:
    visionManager = VisionManager()
    NetworkTables.initialize(server=ROBOT_IP)

    sd = NetworkTables.getTable("SmartDashboard")
    sd.addEntryLisner(visionManager.targetChanged)

    while True:
        time.sleep(1)


finally:
    visionManager.end()



