"""Custom Controller Trigger"""


import wpilib
from .constants import Constants


class Trigger(object):
    """Custom Controller Trigger Class"""

    def __init__(self, trigger_number, joystick_port):
        self.trigger_number = trigger_number
        self.joystick_port = joystick_port
        self.driver_station = wpilib.DriverStation.getInstance()
        self._previous_press = False
        self._held = False
        self._toggled = False

    @property
    def true_value(self):
        """The value of the Axis after reversal and before deadband calculations"""
        return self.driver_station.getStickAxis(self.joystick_port, self.trigger_number)

    @property
    def filtered_value(self):
        """The value of the Axis after reversal and deadband calculations"""
        true_value = self.true_value

        if abs(true_value) >= Constants.TRIGGER_DEADBAND:
            return true_value
        else:
            return 0

    @property
    def pressed(self):
        """Whether or not the Trigger is pressed"""
        return self.driver_station.getStickAxis(self.joystick_port, self.trigger_number) > Constants.TRIGGER_DEADBAND

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
