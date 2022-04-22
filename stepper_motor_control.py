# sends new stepper motor positions to the SKR

import time
import serial
import sys
from . import initialization as init

# homes the axes
def home_SKR():
    command = "G28"
    set_stepper_motors(command)
    time.sleep(30)

# sets X/Y positions for gantry and Z position for end-effector
# arguments are optional
def send_SKR_command(x_pos = None, y_pos = None, z_pos = None):
    command = "G1"
    
    if x_pos != None:
        command += " X" + str(x_pos)
    if y_pos != None:
        command += " Y" + str(y_pos)
    if z_pos != None:
        command += " Z" + str(z_pos)
        
    print(command)
    set_stepper_motors(command)
    
# send to SKR
def set_stepper_motors(stepper_commands):
    stepper_commands += '\n'
    init.SKR_port.write(stepper_commands.encode())
    SKR_echo = init.SKR_port.readline()
    print(SKR_echo)
  
