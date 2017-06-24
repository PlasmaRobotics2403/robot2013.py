"""Custom Controller Button"""


import wpilib
from .constants import Constants


class Button(object):
    """Custom Controller Button Class"""

    def __init__(self, button_number, joystick_port):
        self.button_number = button_number
        self.joystick_port = joystick_port
        self.driver_station = wpilib.DriverStation.getInstance()
        self._previous_press = False
        self._toggled = False

    @property
    def pressed(self):
        """Whether or not the Button is pressed"""
        return self.driver_station.getStickButton(self.joystick_port, self.button_number)

    @property
    def held(self):
        """Whether or not the Button has been pressed for one or more iterative tick"""
        if self.pressed:
            if self._previous_press:
                return True
            else:
                self._previous_press = True
                return False
        else:
            self._previous_press = False
            return False

    @property
    def off_to_on(self):
        """Rising Edge Detector: Whether or not the Button has been switched from Off to On"""
        return self.pressed and not self.held

    @property
    def on_to_off(self):
        """Falling Edge Detector: Whether or not the Button has been switched from On to Off"""
        return self.held and not self.pressed

    @property
    def toggled(self):
        """Whether or not the Button has been toggled"""
        if self.on_to_off:
            self._toggled = not self._toggled
        return self._toggled
