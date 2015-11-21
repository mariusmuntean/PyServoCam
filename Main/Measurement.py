# -*- coding: utf-8 -*-


class Measurement(object):
    def __init__(self, panAngle, tiltAngle, distanceCm, imageName):
        self.panAngle = panAngle
        self.tiltAngle = tiltAngle
        self.distanceCm = distanceCm
        self.imagePath = imageName

    def __json__(self):
        return dict(
            panAngle=self.panAngle,
            tiltAngle=self.tiltAngle,
            distanceCm=self.distanceCm,
            imagePath=self.imagePath
        )
