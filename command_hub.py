# command hub for Jetson Nano
# communicates with Mega, Uno, and SKR boards
# for Mega, sends command of 4 values indicating velocity for each DC motor (deg/sec per motor)
# for Uno, sends command of 2 values indicating direction of linear actuators (pair and solo LAs)
# for SKR, sends command of 3 values indicating stepper motor positions (X, Y, Z)

from initialization import *
# from DC_motor_control import *
from linear_actuator_control import *
from stepper_motor_control import *

if __name__ == '__main__':
    # open USB ports
    (mega_port, uno_port, SKR_port) = initialize_ports()

    while (1):
        # grab input for DC motors and send to Mega
        # set_DC_motors(mega_port)
  
        # grab input for linear actuators and send to Uno
        set_linear_actuators(uno_port)
  
        # grab input for stepper motors and send to SKR
        set_stepper_motors(SKR_port)
