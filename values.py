"""Easily Modifiable Values for use throughout the Robot Control Code"""

class Values(object):
    """Values within this class are accessible as class attributes throughout the Robot Control Code"""

    # Controller IDs
    CONTROLLER_ID = 0

    # Drive Motor CAN IDs
    DRIVE_LEFT_MAIN_ID = 2
    DRIVE_LEFT_SLAVE_ID = 3
    DRIVE_RIGHT_MAIN_ID = 4
    DRIVE_RIGHT_SLAVE_ID = 5

    # Shooter Motor CAN IDs
    SHOOT_FRONT_ID = 6
    SHOOT_BACK_ID = 7

    # Shooter Solenoid Port IDs
    SHOOT_SOLENOID_FORWARD_CHANNEL_ID = 0
    SHOOT_SOLENOID_REVERSE_CHANNEL_ID = 1

    # Drive Train Configuration
    DRIVE_SPEED_MULTIPLIER = 1
    DRIVE_TURN_MULTIPLIER = 0.9

    # Shooter Configuration]
    SHOOTER_SPEED_INTERVALS = 5
    SHOOTER_DEFAULT_SPEED_STATE = 2 # possible values [0,1,2,3,4]
    SHOOTER_MIN_SPEED = 0.35
    SHOOTER_MAX_SPEED = 0.95
