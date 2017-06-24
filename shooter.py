"""Defines the Shooter used within the Robot Control Code"""


import wpilib # Base WPI-Lib package
import ctre # Cross The Road Electronics Modules

from values import Values


class Shooter(object):
    """Custom Shooter Class for use with Frobo"""

    def __init__(self, robot, talon_front_id, talon_back_id, solenoid_forward_id, solenoid_reverse_id):

        self.robot = robot # Reference from the main robot instance

        # Initialize Shooter Motor Controllers
        self.talon_front = ctre.CANTalon(talon_front_id)
        self.talon_back = ctre.CANTalon(talon_back_id)

        # Set Back Motor to Follower Mode
        self.talon_back.changeControlMode(ctre.CANTalon.ControlMode.Follower)
        self.talon_back.set(self.talon_front.getDeviceID())

        # Initialize Shooter Solenoid
        self.solenoid_shoot = wpilib.DoubleSolenoid(solenoid_forward_id, solenoid_reverse_id)

        # Initialize State Attributes
        self.enabled = False
        self.speed_state = Values.SHOOTER_DEFAULT_SPEED_STATE
        self.piston_state = 0

        # Calculate Speed State Values
        max_speed = min(Values.SHOOTER_MAX_SPEED, 1)
        min_speed = max(Values.SHOOTER_MIN_SPEED, 0)
        val_step = (max_speed - min_speed) / float(4)
        self.speed_range = [round(min_speed + (val_num * val_step), 2) for val_num in range(Values.SHOOTER_SPEED_INTERVALS - 1)] + [max_speed]

    def update(self, controller):
        """Updates Shooter States regarding wheel power and solenoid firing"""

        self.enabled = controller.A.toggled

        if self.enabled:
            if controller.DPAD.up:
                if not (self.speed_state == Values.SHOOTER_SPEED_INTERVALS - 1):
                    self.speed_state += 1
            elif controlelr.DPAD.down:
                if not self.speed_state == 0:
                    self.speed_state -= 1

            self.talon_front.set(self.speed_range[self.speed_state])

        if controller.RB.pressed:
            self.fire()

        if not controller.RB.pressed:
            self.retract()

    def enable(self):
        """Handles enabling of the shooter"""
        self.enabled = True

    def disable(self):
        """Handles disabling of the shooter"""
        self.enabled = False

    def fire(self):
        """Handles firing of the shooter solenoid"""
        if self.enabled:
            if self.solenoid_shoot.isFwdSolenoidBlackListed():
                self.driver_station.reportError('[SHOOTER] Error: Forward Solenoid is Blacklisted')
            elif self.solenoid_shoot.isRevSolenoidBlackListed():
                self.driver_station.reportError('[SHOOTER] Error: Reverse Solenoid is Blacklisted')
            else:
                self.solenoid_shoot.set(wpilib.DoubleSolenoid.Value.kForward)

    def retract(self):
        """Handles the retracting of the shooter solenoid"""
        self.solenoid_shoot.set(wpilib.DoubleSolenoid.Value.kReverse)
