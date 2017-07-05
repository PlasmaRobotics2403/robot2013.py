"""Defines the Drive Train used within the Robot Control Code"""


import wpilib # Base WPI-Lib package
import ctre # Cross The Road Electronics Modules

from values import Values


class FroboDrive(object):
    """Custom Drive Train Class for use with Frobo"""

    def __init__(self, robot, left_main_id, left_slave_id, right_main_id, right_slave_id):

        self.robot = robot # Reference to the main robot instance

        # Initialize Drive Train Motors
        self.talon_left_main = ctre.CANTalon(left_main_id)
        self.talon_left_slave = ctre.CANTalon(left_slave_id)
        self.talon_right_main = ctre.CANTalon(right_main_id)
        self.talon_right_slave = ctre.CANTalon(right_slave_id)

        # Set Slave Motors to Follower Mode
        self.talon_left_slave.changeControlMode(ctre.CANTalon.ControlMode.Follower)
        self.talon_left_slave.set(self.talon_left_main.getDeviceID())
        self.talon_right_slave.changeControlMode(ctre.CANTalon.ControlMode.Follower)
        self.talon_right_slave.set(self.talon_right_main.getDeviceID())

        # Invert Right Talon Direction
        self.talon_right_main.setInverted(True)

        # Driver Station Instance
        self.driver_station = wpilib.DriverStation.getInstance()


    def fps(self, *, power_axis=None, turn_axis=None, power_value=None, turn_value=None):
        """FPS-Style Drive Control Method"""

        if power_axis or turn_axis:
            if not power_axis and turn_axis:
                self.driver_station.reportError('[FroboDrive] ERROR: If joystick axis are provided, both power_axis and turn_axis must be provided.')
                return
            power_value = power_axis.filtered_value * abs(power_axis.filtered_value)
            turn_value = turn_axis.filtered_value * abs(turn_axis.filtered_value)
        elif not (power_value and turn_value):
            self.driver_station.reportError('[FroboDrive] ERROR: If joystick axis are not provided, both power_value and turn_value must be provided.')
            return

        turn_multiplier = abs(Values.DRIVE_TURN_MULTIPLIER) if abs(Values.DRIVE_TURN_MULTIPLIER) < 1 else 1
        turn_value = turn_value * turn_multiplier

        speed_multiplier = abs(Values.DRIVE_SPEED_MULTIPLIER) if abs(Values.DRIVE_SPEED_MULTIPLIER) < 1 else 1
        power_value = power_value * speed_multiplier

        left_speed = power_value + turn_value
        right_speed = power_value - turn_value

        self.talon_left_main.set(left_speed)
        self.talon_right_main.set(right_speed)
