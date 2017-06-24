"""Custom Joystick Class"""


from .constants import Constants

from .button import Button
from .axis import Axis
from .dpad import DPad
from .trigger import Trigger


class Joystick(object):
    """Custom Joystick Class"""

    def __init__(self, port):
        self._port = port

        self.A = Button(Constants.JOYSTICK_A_ID, port)
        self.B = Button(Constants.JOYSTICK_B_ID, port)
        self.X = Button(Constants.JOYSTICK_X_ID, port)
        self.Y = Button(Constants.JOYSTICK_Y_ID, port)
        self.LB = Button(Constants.JOYSTICK_LB_ID, port)
        self.RB = Button(Constants.JOYSTICK_RB_ID, port)
        self.BACK = Button(Constants.JOYSTICK_BACK_ID, port)
        self.START = Button(Constants.JOYSTICK_START_ID, port)
        self.L3 = Button(Constants.JOYSTICK_L3_ID, port)
        self.R3 = Button(Constants.JOYSTICK_R3_ID, port)

        self.LEFTX = Axis(Constants.JOYSTICK_LEFTX_ID, port)
        self.LEFTY = Axis(Constants.JOYSTICK_LEFTY_ID, port, True)
        self.RIGHTX = Axis(Constants.JOYSTICK_RIGHTX_ID, port)
        self.RIGHTY = Axis(Constants.JOYSTICK_RIGHTY_ID, port, True)

        self.DPAD = DPad(Constants.JOYSTICK_DPAD_ID, port)

        self.LT = Trigger(Constants.JOYSTICK_LT_ID, port)
        self.RT = Trigger(Constants.JOYSTICK_RT_ID, port)

    @property
    def port(self):
        """The Port of the represented Joystick"""
        # This property is not 100% needed, but is included instead of making the raw variable public to prevent people from accidentally overwriting the port and screwing up this representative value
        return self._port
