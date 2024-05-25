# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Surya Gedipudi                                               #
# 	Description:  Project 5: Controlling Lift Arm                              #
#                                                                              #
# ---------------------------------------------------------------------------- #

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

def liftArm(velocity, liftDisp):   # vel = motor velocity, mDisp = angular displacement of motor shaft
                                   # liftDisp = angular displacement for lift

    # Set motor power level
    liftMotor.set_velocity(velocity, PERCENT)

    # Configure the motor to hold its position once the lift arm rotation is complete.
    liftMotor.set_stopping(HOLD)

    GR = 5                      # Input gear = 12T, output gear = 60T for lift arm
    motorDisp = liftDisp * GR   # Corresponding angular disp. of motor shaft with a GR = 5

    # Print starting potentiometer position (degrees)
    initPos = pot1.angle(DEGREES)
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Pot. Angle: " + str(initPos))

    # Rotate the lift arm
    liftMotor.spin_for(FORWARD, motorDisp, DEGREES)

    # Print final potentiometer position (degrees)
    finalPos = pot1.angle(DEGREES)
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Pot. Angle: " + str(finalPos))

    # Print liftarm's angular displacement
    brain.screen.set_cursor(3, 1)
    brain.screen.print("Angular Displacement: " + str(abs(finalPos - initPos)))

def main():

    liftVel = 20            # Lift motor velocity in percent
    bump()                  # param1 = velocity level
    liftArm(liftVel, 55)    # param2 = desired angular displacement of lift in degrees (+ raise, - lower)


main()
