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
endAngle = 180.0

panTilt.panTo(currentAngle)
time.sleep(1)

while currentAngle < endAngle:
    currentAngle += 15.0
    panTilt.panTo(currentAngle)
    time.sleep(0.5)

panTilt.panCenter()