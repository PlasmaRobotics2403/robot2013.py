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
    def held(self):
        """Whether or not the Trigger has been pressed for one or more iterative tick"""
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
        """Rising Edge Detector: Whether or not the Trigger has been switched from Off to On"""
        return self.pressed and not self.held

    @property
    def on_to_off(self):
        """Falling Edge Detector: Whether or not the Trigger has been switched from On to Off"""
        return self.held and not self.pressed

    @property
    def toggled(self):
        """Whether or not the Trigger has been toggled"""
        if self.on_to_off:
            self._toggled = not self._toggled
        return self._toggled
