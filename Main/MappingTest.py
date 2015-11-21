#!/usr/bin/python

from PanTiltDriver import PanTiltDriver
from SR04 import SR04
from Measurement import Measurement
import json
import picamera
import time
import os

# Set mapping root dir on Desktop
# mappingRootDir = os.path.expanduser("~/Desktop/mapping")
mappingRootDir = os.path.expanduser("/home/pi/Desktop/mapping")
currentMappingDir = mappingRootDir + "/" + str(time.time())

# Make sure the dir exists
if not os.path.exists(currentMappingDir):
    os.makedirs(currentMappingDir)

# Create xml mapping file
mappingFilePath = currentMappingDir + "/mapping.json"
open(mappingFilePath, 'w')

# Init the hardware
sensor = SR04(33, 35)
panTilt = PanTiltDriver()
piCam = picamera.PiCamera()

# Init some params
sweepStepSize = 30.0  # In Degrees
sweepStepDuration = 0.5  # In seconds
currentPanAngle = 0.0

# Go to initial position
panTilt.panLeft()
time.sleep(sweepStepDuration)
panTilt.tiltDown()
time.sleep(sweepStepDuration)

# Take a 180 degree sweep

measurements = []
while currentPanAngle < 180.0:
    # Take measurement and add it to the list
    imageFilePath = currentMappingDir + "/" + str(time.time()) + ".jpg"
    piCam.capture(imageFilePath)
    distance = sensor.getDistanceCM()
    measurement = Measurement(currentPanAngle, 0.0, distance, imageFilePath)
    measurements.append(measurement)

    # Continue sweep
    currentPanAngle += sweepStepSize
    panTilt.panTo(currentPanAngle)
    time.sleep(sweepStepDuration)

# Persist measurements array/list to a file
with open(mappingFilePath, 'w') as outfile:
    tempDump = json.dumps(measurements[0].__dict__)
    json.dump([m.__dict__ for m in measurements], outfile)
