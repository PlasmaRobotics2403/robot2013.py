"""Custom Controller Button"""


import wpilib
from .constants import Constants


class Button(object):
    """Custom Controller Button Class"""

    def __init__(self, button_number, joystick_port):
        self.button_number = button_number
        self.joystick_port = joystick_port
        self.driver_station = wpilib.DriverStation.getInstance()
        self._held = False
        self._toggled = False

    @property
    def pressed(self):
        """Whether or not the Button is pressed"""
        return self.driver_station.getStickButton(self.joystick_port, self.button_number)

    @property
    def off_to_on(self):
        """Rising Edge Detector: Whether or not the Button has been switched from Off to On"""
        if self.pressed and not self._held:
            self._held = True
            return True
        else:
            self._held = self.pressed
            return False

    @property
    def on_to_off(self):
        """Falling Edge Detector: Whether or not the Button has been switched from On to Off"""
        if self._held and not self.pressed:
            self._held = True
            return True
        else:
            self._held = self.pressed
            return False

    @property
    def toggled(self):
        """Whether or not the Button has been toggled"""
        if self.off_to_on:
            self._toggled = not self._toggled
        return self._toggled
