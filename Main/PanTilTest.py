#!/usr/bin/python

from PanTiltDriver import PanTiltDriver
import time

panTilt = PanTiltDriver()

# while (True):
#     panTilt.panLeft()
#     time.sleep(1)
#     panTilt.panCenter()
#     time.sleep(1)
#     panTilt.panRight()
#     time.sleep(1)
#     panTilt.panCenter()
#     time.sleep(1)


currentAngle = 0.0
endAngle = 45.0

panTilt.tiltTo(0.0)
panTilt.panCenter()
time.sleep(1)

while currentAngle < endAngle:
    currentAngle += 5.0
    panTilt.tiltTo(currentAngle)
    time.sleep(0.2)

panTilt.panCenter()
panTilt.tiltUp()
time.sleep(0.5)
