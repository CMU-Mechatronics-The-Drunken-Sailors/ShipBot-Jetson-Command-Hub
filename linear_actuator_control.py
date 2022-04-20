# sets linear actuators to one of four positions, described below

import serial
import sys
from . import initialization as init

# LA pair retracted (R), LA solo retracted (R) -> -255 -255 -> arm is bent, tip is straight
def retract_pair_retract_solo():
    set_linear_actuators("-255 -255")

# LA pair retracted (R), LA solo extended (E) -> -255 255 -> arm and tip are bent
def retract_pair_extend_solo():
    set_linear_actuators("-255 255")

# LA pair extended (E), LA solo retracted (R) -> 255 -255 -> arm and tip are straight
def extend_pair_retract_solo():
    set_linear_actuators("255 -255")

# LA pair extended (E), LA solo extended (E) -> 255 255 -> arm is straight, tip is bent
def extend_pair_extend_solo():
    set_linear_actuators("255 255")
    
# sets linear actuators, given string
def set_linear_actuators(LA_commands):    
    # send to Uno
    LA_commands += '\n'
    init.uno_port.write(LA_commands.encode())
    uno_echo = init.uno_port.readline()
    print(uno_echo)  
