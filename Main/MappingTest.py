#!/usr/bin/python

import os
import time

import picamera

import ParseConfig
from Measurement import Measurement
from PanTiltDriver import PanTiltDriver
from SR04 import SR04
from parse_rest.connection import register

# Set mapping root dir on Desktop
# mappingRootDir = os.path.expanduser("~/Desktop/mapping")
from parse_rest.datatypes import Object, File

mappingRootDir = os.path.expanduser("/home/pi/Desktop/mapping")
currentMappingDir = mappingRootDir + "/" + str(time.time())

# Make sure the dir exists
if not os.path.exists(currentMappingDir):
    os.makedirs(currentMappingDir)

# Create xml mapping file
# mappingFilePath = currentMappingDir + "/mapping.json"
# open(mappingFilePath, 'w')

# Init the hardware
sensor = SR04(33, 35)
panTilt = PanTiltDriver()
piCam = picamera.PiCamera()

# Init some params
panStepSize = 30.0  # In Degrees
tiltStepSize = 15.0  # In Degrees
panStepDuration = 0.5  # In seconds
tiltStepDuration = 0.5  # In seconds
currentPanAngle = 0.0
currentTiltAngle = 0.0

# Go to initial position
panTilt.panLeft()
time.sleep(panStepDuration)
panTilt.tiltUp()
time.sleep(panStepDuration)

# Take a 180 degree sweep
measurements = []
try:
    while currentTiltAngle <= 45.0:
        while currentPanAngle < 180.0:
            # Take measurement and add it to the list
            imageFilePath = currentMappingDir + "/" + str(time.time()) + ".jpg"
            piCam.capture(imageFilePath)
            distance = sensor.getDistanceCM()
            measurement = Measurement(currentPanAngle, currentTiltAngle, distance, imageFilePath)
            measurements.append(measurement)

            # Continue sweep
            currentPanAngle += panStepSize
            panTilt.panTo(currentPanAngle)
            time.sleep(panStepDuration)
        # Increase tilt
        currentTiltAngle += tiltStepSize
        panTilt.tiltTo(currentTiltAngle)
        time.sleep(tiltStepDuration)
        # Start again from the right
        currentPanAngle = 0.0
        panTilt.panTo(currentPanAngle)
        time.sleep(3 * panStepDuration)
finally:
    # Clean up and return to neutral position
    piCam.close()
    panTilt.panCenter()
    panTilt.tiltUp()
    time.sleep(panStepDuration)


# Persist the measurements to Parse, yay!

# Init Parse
register(ParseConfig.ApplicationId, ParseConfig.RestApiKey)

# Save all images to Parse
files = []
for idx in range(len(measurements)):
    imageName = str(measurements[idx].panAngle) + "_" + str(measurements[idx].tiltAngle) + ".jpg"
    currentImageParseFile = File(imageName, open(measurements[idx].imagePath, 'rb').read(),'image/jpeg')
    print('Saving {0} to Parse.com'.format(imageName))
    currentImageParseFile.save()
    files.append(currentImageParseFile)

# Associate the image with the measurement and save all
parseMeasurements = []
ParseMeasurement = Object.factory("Measurement")
for idx in range(len(measurements)):
    parseMeasurement = ParseMeasurement()
    print('Persisting measurement {0} to pParse.com'.format(measurements[idx]))
    parseMeasurement.panAngle = measurements[idx].panAngle
    parseMeasurement.tiltAngle = measurements[idx].tiltAngle
    parseMeasurement.distanceCm = measurements[idx].distanceCm
    parseMeasurement.image = files[idx]
    parseMeasurement.save()
    parseMeasurements.append(parseMeasurement)

# Save everything under one instance of the Mapping class
ParseMapping = Object.factory("Mapping")
newParseMapping = ParseMapping()
newParseMapping.measurements = parseMeasurements
newParseMapping.save()
print('Saved mapping: {0} to Parse.com'.format(newParseMapping))
