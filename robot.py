"""Drive Code for Plasma Robotics' 2013 Competition Robot (Frobo), written using robot.py with the 2015+ controll system.
   Written and Tested by Team 2403 members including Evin Harris and Nicholas Ardavin"""


import wpilib # Base WPI-Lib package
import ctre # Cross The Road Electronics Modules

from values import Values
from drive import FroboDrive
from shooter import Shooter
from controller import Joystick


class Frobo(wpilib.IterativeRobot):
    """Control code for Frobo, the 2013 Competition Robot of FRC Team 2403 (Plasma Robotics)"""

    def robotInit(self):
        """Initialization method for the Frobo class.  Initializes objects needed elsewhere throughout the code."""

        # Initialize Joystick
        self.controller = Joystick(Values.CONTROLLER_ID)

        # Initialize Drive Sub-System
        self.drive = FroboDrive(self, Values.DRIVE_LEFT_MAIN_ID, Values.DRIVE_LEFT_SLAVE_ID, Values.DRIVE_RIGHT_MAIN_ID, Values.DRIVE_RIGHT_SLAVE_ID)

        # Initialize Shooter Sub-System
        self.shooter = Shooter(self, Values.SHOOT_FRONT_ID, Values.SHOOT_BACK_ID, Values.SHOOT_SOLENOID_FORWARD_CHANNEL_ID, Values.SHOOT_SOLENOID_REVERSE_CHANNEL_ID)

    def robotPeriodic(self):
        pass

    # DISABLED MODE

    def disabledInit(self):
        """Method ran when Frobo first enters the *disabled* mode."""
        pass

    def disabledPeriodic(self):
        """Method that runs while Frobo is in the *disabled* mode."""
        pass


    # AUTONOMOUS MODE

    def autonomousInit(self):
        """Method ran when Frobo first enters the *autonomous* mode."""
        pass

    def autonomousPeriodic(self):
        """Method that runs while Frobo is in the *autonomous* mode."""
        pass


    # TELEOP MODE

    def teleopInit(self):
        """Method ran when Frobo first enters the *teleop* mode."""
        self.shooter.disable()

    def teleopPeriodic(self):
        """Method that runs while Frobo is in the *teleop* mode."""
        self.drive.fps(power_axis=self.controller.LEFTY, turn_axis=self.controller.RIGHTX)
        self.shooter.update(self.controller)

    # TEST MODE

    def testInit(self):
        """Method ran when Frobo first enters the *test* mode."""
        pass

    def testPeriodic(self):
        """Method that runs while Frobo is in the *test* mode."""
        pass


if __name__ == '__main__':
    wpilib.run(Frobo)
