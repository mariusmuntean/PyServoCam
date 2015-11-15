#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 104  # Min pulse length out of 4096
servoMid = 270
servoMax = 380  # Max pulse length out of 4096


pwm.setPWMFreq(50)                        # Set frequency to 50 Hz
while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(3, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(3, 0, servoMid)
  time.sleep(1)
  pwm.setPWM(3, 0, servoMax)
  time.sleep(1)
  pwm.setPWM(3, 0, servoMid)
  time.sleep(1)



