# sends new linear actuator commands to the Uno

import serial
import sys

def set_linear_actuators(uno_port):
    LA_commands = input("Linear Actuator Commands:\n")

    if LA_commands == '':
        return

    LA_commands += '\n'
    uno_port.write(LA_commands.encode())
    uno_echo = uno_port.readline()
    print(uno_echo)  
