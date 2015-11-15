#!/usr/bin/python

from PanTiltDriver import PanTiltDriver
import time



panTilt = PanTiltDriver()

while (True):
    panTilt.panLeft()
    time.sleep(1)
    panTilt.panCenter()
    time.sleep(1)
    panTilt.panRight()
    time.sleep(1)
    panTilt.panCenter()
    time.sleep(1)


