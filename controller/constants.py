"""Easily Modifiable Values for use within the controler module"""

class Constants(object):
    """Controller Related Constants"""

    # DEADBANDS
    AXIS_DEADBAND = 0.15 # The Minimum Value at which the AXIS will recognize interaction
    TRIGGER_DEADBAND = 0.1 # The Minimum Value at which the TRIGGER will recognize interaction

    # JOYSTICK ID CONSTANTS
    JOYSTICK_A_ID = 1
    JOYSTICK_B_ID = 2
    JOYSTICK_X_ID = 3
    JOYSTICK_Y_ID = 4
    JOYSTICK_LB_ID = 5
    JOYSTICK_RB_ID = 6
    JOYSTICK_BACK_ID = 7
    JOYSTICK_START_ID = 8
    JOYSTICK_L3_ID = 9
    JOYSTICK_R3_ID = 10

    JOYSTICK_LEFTX_ID = 0
    JOYSTICK_LEFTY_ID = 1
    JOYSTICK_RIGHTX_ID = 4
    JOYSTICK_RIGHTY_ID = 5

    JOYSTICK_DPAD_ID = 0

    JOYSTICK_LT_ID = 2
    JOYSTICK_RT_ID = 3
