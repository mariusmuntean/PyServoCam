

class Measurement(object):
    def __init__(self, panAngle, tiltAngle, distanceCm, imageName):
        self.panAngle = panAngle
        self.tiltAngle = tiltAngle
        self.distanceCm = distanceCm
        self.imagePath = imageName
