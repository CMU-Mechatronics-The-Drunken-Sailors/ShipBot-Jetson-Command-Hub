# sends new stepper motor positions to the SKR

import serial
import sys
import initialization as init

# sets X/Y positions for gantry and Z position for end-effector
# arguments are optional
def build_command(x_pos = None, y_pos = None, z_pos = None):
    command = "G1"
    
    if x_pos != None:
        command += " X" + str(x_pos)
    elif y_pos != None:
        command += " Y" + str(y_pos)
    elif z_pos != None:
        command += " Z" + str(z_pos)
        
    set_stepper_motor(command)
    
# send to SKR
def set_stepper_motors(stepper_commands):
    stepper_commands += '\n'
    init.write(stepper_commands.encode())
    SKR_echo = init.readline()
    print(SKR_echo)
  
