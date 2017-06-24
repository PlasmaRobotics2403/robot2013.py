"""Custom Controller DPad"""


import wpilib
from .constants import Constants


class DPad(object):
    """Custom Controller DPad Class"""

    def __init__(self, dpad_number, joystick_port):
        self.dpad_number = dpad_number
        self.joystick_port = joystick_port
        self.driver_station = wpilib.DriverStation.getInstance()

    @property
    def angle(self):
        """The Angle of the DPad"""
        return self.driver_station.getStickPOV(self.joystick_port, self.dpad_number)

    @property
    def up(self):
        """Whether or not the angle of the d-pad is *up*"""
        return self.angle == 0

    @property
    def up_right(self):
        """Whether or not the angle of the d-pad is *up* and *right*"""
        return self.angle == 45

    @property
    def right(self):
        """Whether or not the angle of the d-pad is *right*"""
        return self.angle == 90

    @property
    def down_right(self):
        """Whether or not the angle of the d-pad is *down* and *right*"""
        return self.angle == 135

    @property
    def down(self):
        """Whether or not the angle of the d-pad is *down*"""
        return self.angle == 180

    @property
    def down_left(self):
        """Whether or not the angle of the d-pad is *down* and *left*"""
        return self.angle == 225

    @property
    def left(self):
        """Whether or not the angle of the d-pad is *left*"""
        return self.angle == 270

    @property
    def up_left(self):
        """Whether or not the angle of the d-pad is *up* and *left*"""
        return self.angle == 315
