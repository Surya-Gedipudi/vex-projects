# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Surya Gedipudi                                               #
# 	Description:  Project 2: Velocity Levels                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

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

# Spin motors
def spinMotors(velocity):

    # Set velocity for left and right motors
    rightMotor.set_velocity(velocity, PERCENT)
    leftMotor.set_velocity(velocity, PERCENT)

    # Spin motor
    rightMotor.spin(FORWARD)
    leftMotor.spin(FORWARD)

    # Display timer start
    brain.timer.clear()
    brain.screen.print("Timer Started")

# Stop Motors
def stopMotors():
    rightMotor.stop()
    leftMotor.stop()

# Main
def main():

    motorVelocity = 70  # Velocity in % (max v = 200 rpm);   For this project, motorVelocity is modified here.
    brain.screen.set_cursor(1, 1)

    bump()      # Wait for the bump switch to be pressed
    
    spinMotors(motorVelocity)
    wait(3250, MSEC)    # Wait States
    stopMotors()

    brain.screen.set_cursor(2, 1)   # moves cursor down to next row
    brain.screen.print("Time: " + str(brain.timer.time(SECONDS)))

main()  # Call main function