# --------------------------------------------------------------------------------- #
#                                                                                   #
# 	Module:       main.py                                                           #
# 	Author:       Surya Gedipudi                                                    #
# 	Description:  Project 4: Turning with Encoders                                  #
#                                                                                   #
# --------------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()


# Robot configuration code
rightMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
leftMotor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
liftMotor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
rightEncoder = Encoder(brain.three_wire_port.a)
leftEncoder = Encoder(brain.three_wire_port.g)
pot1 = PotentiometerV2(brain.three_wire_port.e)
bumpSwitch = Bumper(brain.three_wire_port.d)

# Bump Switch - will hold program until pressed
def bump():
    while (bumpSwitch.pressing() == False):
        wait(10, MSEC)  # Debounce the button (10 milliseconds)
        pass

#spin motors
def spinMotors(rightMotorVelocity, leftMotorVelocity):

    # Set velocities for left and right motors
    rightMotor.set_velocity(rightMotorVelocity, PERCENT)
    leftMotor.set_velocity(leftMotorVelocity, PERCENT)

    # Spin motors
    rightMotor.spin(FORWARD)
    leftMotor.spin(FORWARD)

#stop motors
def stopMotors():
    rightMotor.stop()
    leftMotor.stop()

# Left Swing Turn
def swingLeft(turnCount):                               # turnCount - encoder count for turn
    rightEncoder.set_position(0, DEGREES);              # Reset the right encoder to 0.

    while (rightEncoder.position(DEGREES) < turnCount): # Check turn status based on right encoder count
        spinMotors(50, 0)                               # Spin right motor forward (left = off)

    stopMotors()                                        # Stop the motors

# Left Swing Turn
def swingRight(turnCount):                              # turnCount - encoder count for turn
    leftEncoder.set_position(0, DEGREES);               # Reset the left encoder to 0.

    while (leftEncoder.position(DEGREES) < turnCount):  # Check turn status based on left encoder count
        spinMotors(60, 0)                               # Spin left motor forward (right = off)

    stopMotors()                                        # Stop the motors

# Left Point Turn
def pointLeft(turnCount):                               # turnCount = encoder count for turn
    rightEncoder.set_position(0, DEGREES)               # Reset the right encoder to 0

    while (rightEncoder.position(DEGREES) < turnCount): # Check turn status based on right encoder count
        spinMotors(60, -60)                             # Spin right motor forward and left reverse

    stopMotors()                                        # Stop the motors

# Right Point Turn
def pointRight(turnCount):                              # turnCount = encoder count for turn
    leftEncoder.set_position(0, DEGREES)                # Reset the left encoder to 0

    while (leftEncoder.position(DEGREES) < turnCount):  # Check turn status based on left encoder count
        spinMotors(-50, 50)                             # Spin left motor forward and right reverse

    stopMotors()                                        # Stop the motors                                

# Activity 4 will have to examine the swingLeft() and pointLeft functions separately.
def main():
    bump()              # Wait for bump switch to be pressed to start the motors
    swingLeft(50)      # degree swing turn (count value specific to robot)
                        # Count for 90-deg. left turn may not equal count for 90-deg. right turn

    pointLeft(690)      # degree point turn (count value specific to robot)
    # Count for deg. left turn may not equal count for 90-deg. right turn

main()
