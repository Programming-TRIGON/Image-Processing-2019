from scvf import cv_loop
from scvf.io import NetworkTableIO

from HatchPipeLine import GripPipeline as HatchPipeLine
#from RetroflectorPipeLine import GripPipeline as RetroflectorPipeLine

nt_io = NetworkTableIO("10.59.90.2", "ImageProcessing")

pipelines = {"hatch": HatchPipeLine()} #"cargo": RetroflectorPipeLine(),

cv_loop.start(pipelines, output_consumer=nt_io.output_consumer, settings_supplier=nt_io.settings_supplier, camera_port=1)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    cv_loop.end()
