from Adafruit_PWM_Servo_Driver import PWM


class PanTiltDriver:
    def __init__(self, customaddress=0x40, panchannel=0, tiltchannel=3):
        self.Address = customaddress
        self.PanChannel = panchannel
        self.TiltChannel = tiltchannel
        self.PanMin = 104
        self.PanMax = 560
        self.TiltMin = 0
        self.TiltMax = 0
        self.PWM = PWM(self.Address)
        self.PWM.setPWMFreq(50)

    def panTo(self, degrees):
        if degrees < 0:
            degrees = 0
        if degrees > 180:
            degrees = 180

        ratio = degrees / float(180)
        panTicks = self.PanMin + (ratio * (self.PanMax - self.PanMin))
        self.PWM.setPWM(self.PanChannel, 0, int(panTicks))

    def tiltTo(self, degrees):
        if degrees < 0:
            degrees = 0
        if degrees > 90:
            degrees = 90

        ratio = degrees / float(90)
        tiltTicks = self.TiltMin + (ratio * (self.TiltMax - self.TiltMin))
        self.PWM.setPWM(self.PanChannel, 0, int(tiltTicks))

    def panLeft(self):
        """Pan completely to the left"""
        self.panTo(0)

    def panCenter(self):
        """Pan to center position"""
        self.panTo(90)

    def panRight(self):
        """Pan completely to the right"""
        self.panTo(180)

    def tiltDown(self):
        """Tilt completely down"""
        self.tiltTo(90)

    def tiltUp(self):
        """Tilt to horizontal position"""
        self.tiltTo(0)
