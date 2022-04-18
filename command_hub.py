# command hub for Jetson Nano
# communicates with Mega, Uno, and SKR boards
# for Mega, sends command of 4 values indicating velocity for each DC motor (deg/sec per motor)
# for Uno, sends command of 2 values indicating direction of linear actuators (pair and solo LAs)
# for SKR, sends command of 3 values indicating stepper motor positions (X, Y, Z)

from initialization import *
from DC_motor_control import *
from linear_actuator_control import *
from stepper_motor_control import *

if __name__ == '__main__':
    # open USB ports
    (mega_port, uno_port, SKR_port) = initialize_ports()
    camera = initialize_camera()

    while (1):
        # send DC motor commands to Mega
        DC_commands = input("DC Motor Commands:\n") # user input for testing/debugging
        if DC_commands == '':
            return
        elif:
            set_DC_motors(mega_port, DC_commands)
  
        # send linear actuators commands to Uno
        LA_commands = input("Linear Actuator Commands:\n") # user input for testing/debugging
        if LA_commands == '':
            return
        elif:
            set_linear_actuators(uno_port, LA_commands)
  
        # send stepper motor commands to SKR
        stepper_commands = input("Stepper Motor Commands:\n") # user input for testing/debugging
        if stepper_commands == '':
            return
        elif:
            set_stepper_motors(SKR_port, stepper_commands)
