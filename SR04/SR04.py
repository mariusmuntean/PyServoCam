import time

import RPi.GPIO as GPIO


class SR04:
    def __init__(self, trigPin, echoPin):
        self.trigPin = trigPin
        self.echoPin = echoPin

        self.initHardware()

    def initHardware(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.trigPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)
        GPIO.output(self.trigPin, False)

        print("Waiting For Sensor To Settle")

        time.sleep(1)

    def getDistanceCM(self):
        # print("Sending TRIG on pin %d" % self.trigPin)

        GPIO.output(self.trigPin, True)

        time.sleep(0.00001)

        GPIO.output(self.trigPin, False)

        # print("Awaiting ECHO on pin %d" % self.echoPin)

        pulse_start = time.time()
        pulse_end = pulse_start

        while GPIO.input(self.echoPin) == 0:
            pulse_start = time.time()

        # print("Measuring ECHO length")
        while GPIO.input(self.echoPin) == 1:
            pulse_end = time.time()

        if pulse_start == pulse_end:
            return 0.0

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17000

        distance = round(distance, 3)

        # print("Distance:", distance, "cm")

        return distance

    def getDistanceCMConservative(self):
        d1 = self.getDistanceCM()
        time.sleep(0.025)
        d2 = self.getDistanceCM()
        return min(d1, d2)

    def cleanUp(self):
        GPIO.cleanup()
