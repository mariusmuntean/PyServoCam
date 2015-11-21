#!/usr/bin/python

from SR04 import SR04

sensor = SR04(23, 24)

dist = sensor.getDistanceCM()

print("Measured %d centimeters", dist)
