# command hub for Jetson Nano
# communicates with Mega, Uno, and SKR boards
# for Mega, sends command of 4 values indicating velocity for each DC motor (deg/sec per motor)
# for Uno, sends command of 2 values indicating direction of linear actuators (pair and solo LAs)
# for SKR, sends command of 3 values indicating stepper motor positions (X, Y, Z)

import time
import cv2
from . import initialization as init
from . import DC_motor_control as Mega
from . import linear_actuator_control as Uno
from . import stepper_motor_control as SKR
from . import realsense_camera as camera

# user input for testing/debugging
def manual_control():
    while (1):
        # send DC motor commands to Mega
        DC_commands = input("DC Motor Commands:\n")
        if DC_commands != '':
            DC_commands += '\n'
            init.mega_port.write(DC_commands.encode())
            mega_echo = init.mega_port.readline()
            print(mega_echo)
  
        # send linear actuators commands to Uno
        LA_commands = input("Linear Actuator Commands:\n") # user input for testing/debugging
        if LA_commands != '':
            if LA_commands == 'RR':
                Uno.retract_pair_retract_solo()
            elif LA_commands == 'RE':
                Uno.retract_pair_extend_solo()
            elif LA_commands == 'ER':
                Uno.extend_pair_retract_solo()
            elif LA_commands == 'EE':
                Uno.extend_pair_extend_solo()
  
        # send stepper motor commands to SKR
        stepper_commands = input("Stepper Motor Commands:\n") # user input for testing/debugging
        if stepper_commands != '':
            SKR.set_stepper_motors(stepper_commands)

def test_camera():
    print("Reading camera...")
    while(1):
        (RGB, depth) = camera.get_image()
        cv2.imshow('RGB', RGB)
        cv2.waitKey(0)
        cv2.imshow('depth', depth)
        cv2.waitKey(0)

if __name__ == '__main__':
    # open USB ports
    init.initialize_ports()
    init.initialize_camera()
    time.sleep(1)

    # grab user input and send to Mega/Uno/SKR
    # manual_control()
    
    test_camera()

    # test DC functions
    # Mega.set_DC_motors(0, 0, 0, 0)
    # while True:
    #     t = time.time()
    #     encoder_ticks = Mega.get_encoder_ticks()
    #     time_to_wait = 0.05 - (time.time() - t)
    #     if time_to_wait < 0:
    #         print("WHOA THIS V BAD")
    #     else:
    #         time.sleep(time_to_wait)
