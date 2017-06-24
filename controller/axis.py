"""Custom Controller Axis"""


import wpilib
from .constants import Constants


class Axis(object):
    """Custom Controller Axis Class"""

    def __init__(self, axis_number, joystick_port, is_reversed=False):
        self.axis_number = axis_number
        self.joystick_port = joystick_port
        self.multiplier = -1 if is_reversed else 1
        self.driver_station = wpilib.DriverStation.getInstance()

    @property
    def true_value(self):
        """The value of the Axis after reversal and before deadband calculations"""
        return self.driver_station.getStickAxis(self.joystick_port, self.axis_number) * self.multiplier

    @property
    def filtered_value(self):
        """The value of the Axis after reversal and deadband calculations"""
        true_value = self.true_value

        if abs(true_value) >= Constants.AXIS_DEADBAND:
            return true_value
        else:
            return 0
