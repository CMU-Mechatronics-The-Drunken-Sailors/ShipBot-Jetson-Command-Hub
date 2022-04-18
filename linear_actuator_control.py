# sends new linear actuator commands to the Uno

import serial
import sys

# sets linear actuators to one of four positions, described below
# LA pair retracted (R), LA solo retracted (R) -> -255 -255 -> arm is bent, tip is straight
# LA pair retracted (R), LA solo extended (E) -> -255 255 -> arm and tip are bent
# LA pair extended (E), LA solo retracted (R) -> 255 -255 -> arm and tip are straight
# LA pair extended (E), LA solo extended (E) -> 255 255 -> arm is straight, tip is bent
def set_linear_actuators(uno_port):
    LA_commands = input("Linear Actuator Commands:\n") # user input for testing/debugging

    # check for one of the four positions above
    if LA_commands == '':
        return
    elif LA_commands == 'RR':
        LA_commands = '-255 -255'
    elif LA_commands == 'RE':
        LA_commands = '-255 255'
    elif LA_commands == 'ER':
        LA_commands = '255 -255'
    elif LA_commands == 'EE':
        LA_commands = '255 255'
        
    # send to Uno
    LA_commands += '\n'
    uno_port.write(LA_commands.encode())
    uno_echo = uno_port.readline()
    print(uno_echo)  
