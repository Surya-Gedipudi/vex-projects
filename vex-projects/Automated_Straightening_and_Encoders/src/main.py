# --------------------------------------------------------------------------------- #
#                                                                                   #
# 	Module:       main.py                                                           #
# 	Author:       Surya Gedipudi                                                    #
# 	Description:  Project 3: Automated Straightening, Encoders, & Velocity Levels   #
#                                                                                   #
# --------------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()


# Robot configuration
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
        wait(10, MSEC)  # Debounce the button
        pass

# DriveStraight compares left and right encoder values, adjusting motors as necessary
def driveStraightForward(distance, overshoot):  # param1 = distance, param2 = overshoot

    distance = distance - overshoot             # Correct the distance traveled
    count = (360 * distance)/(4 * math.pi)      # count = # of degrees to turn 4" dia.
    leftEncoder.set_position(0, DEGREES)        # Reset encoder count values to 0.
    rightEncoder.set_position(0, DEGREES)

    # Normal and slow velocities will be tuned for each robot
    normal = 60     # Normally run at normal% of max speed
    slow = 53       # Run motor at slow% of max. if it is fast compared to other motor

    while (rightEncoder.position(DEGREES) < count):
        encoderValues()

        # Compare left and right encoder values and adjust motor speeds
        # Function: spinMotors(Right Motor Speed, Left Motor Speed)
        if (rightEncoder.position(DEGREES) < leftEncoder.position(DEGREES)):
            spinMotors(normal, slow)    # Spin right @ normal, and left @ slow
        elif (rightEncoder.position(DEGREES) > leftEncoder.position(DEGREES)):
            spinMotors(slow, normal)    # Spin right @ slow, and left @ normal
        else:
            spinMotors(normal, normal)
    stopMotors()

# DriveStraight compares left and right encoder values, adjusting motors as necessary
def driveStraightReverse(distance, overshoot):  # param1 = distance, param2 = overshoot

    distance = distance - overshoot             # Correct the distance traveled
    count = -1 * (360 * distance)/(4 * math.pi)      # count = # of degrees to turn 4" dia.
    leftEncoder.set_position(0, DEGREES)        # Reset encoder count values to 0.
    rightEncoder.set_position(0, DEGREES)

    # Normal and slow velocities will be tuned for each robot
    normal = -50     # Normally run at normal% of max speed
    slow = -43      # Run motor at slow% of max. if it is fast compared to other motor

    while (rightEncoder.position(DEGREES) > count):
        encoderValues()

        # Compare left and right encoder values and adjust motor speeds
        # Function: spinMotors(Right Motor Speed, Left Motor Speed)
        if (rightEncoder.position(DEGREES) < leftEncoder.position(DEGREES)):
            spinMotors(slow, normal)    # Spin right @ normal, and left @ slow
        elif (rightEncoder.position(DEGREES) > leftEncoder.position(DEGREES)):
            spinMotors(normal, slow)    # Spin right @ slow, and left @ normal
        else:
            spinMotors(normal, normal)
    stopMotors()


# Print encoder values to the screen
def encoderValues():
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Right Encoder: ")
    brain.screen.print(rightEncoder.position(DEGREES))
    brain.screen.set_cursor(1, 25)
    brain.screen.print("Left Encoder: ")
    brain.screen.print(leftEncoder.position(DEGREES))

def spinMotors(rightMotorVelocity, leftMotorVelocity):

    # Set velocities for left and right motors
    rightMotor.set_velocity(rightMotorVelocity, PERCENT)
    leftMotor.set_velocity(leftMotorVelocity, PERCENT)

    # Spin motors
    rightMotor.spin(FORWARD)
    leftMotor.spin(FORWARD)

def stopMotors():
    rightMotor.stop()
    leftMotor.stop()

def main():
    bump()  # Wait for bump to be pressed
    driveStraightForward(120, 0) # Distance in inches, Overshoot
    wait(1, SECONDS)
    #driveStraightReverse(120, 55)

main()
