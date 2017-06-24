"""Easily Modifiable Values for use throughout the Robot Control Code"""

class Values(object):
    """Values within this class are accessible as class attributes throughout the Robot Control Code"""

    # Controller IDs
    CONTROLLER_ID = 0

    # Drive Motor CAN IDs
    DRIVE_LEFT_MAIN_ID = 1
    DRIVE_LEFT_SLAVE_ID = 2
    DRIVE_RIGHT_MAIN_ID = 3
    DRIVE_RIGHT_SLAVE_ID = 4

    # Shooter Motor CAN IDs
    SHOOT_FRONT_ID = 5
    SHOOT_BACK_ID = 6

    # Shooter Solenoid Port IDs
    SHOOT_SOLENOID_FORWARD_CHANNEL_ID = 1
    SHOOT_SOLENOID_REVERSE_CHANNEL_ID = 2

    # Drive Train Configuration
    DRIVE_MAX_SPEED = 1
    DRIVE_MAX_TURN = 1

    # Shooter Configuration]
    SHOOTER_SPEED_INTERVALS = 5
    SHOOTER_DEFAULT_SPEED_STATE = 2 # possible values [0,1,2,3,4]
    SHOOTER_MIN_SPEED = 0.35
    SHOOTER_MAX_SPEED = 0.95
