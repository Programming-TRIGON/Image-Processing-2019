from networktables import NetworkTables
from threading import Thread
import logging
import time

ROBOT_IP = '10.59.90.2'





logging.basicConfig(level=logging.DEBUG)

try:
    NetworkTables.initialize(server=ROBOT_IP)

    sd = NetworkTables.getTable("SmartDashboard")
    sd.addEntryLisner(targetChanged)

    while True:
        time.sleep(1)


finally:
    pass



