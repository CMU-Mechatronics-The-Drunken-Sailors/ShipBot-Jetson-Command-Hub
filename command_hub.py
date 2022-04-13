# command hub for Jetson Nano
# communicates with Mega, Uno, and SKR boards
# for Mega, sends command of 4 values indicating velocity for each DC motor (deg/sec per motor)
# for Uno, sends command of 2 values indicating direction of linear actuators (pair and solo LAs)
# for SKR, sends command of 3 values indicating stepper motor positions (X, Y, Z)

import serial
import serial.tools.list_ports
import sys

# open ports
def initialize_ports():
    BAUD_RATE = 115200
    mega_port = uno_port = SKR_port = None

    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)

        if "Mega" in p.description:
            mega_port = serial.Serial(p.device, BAUD_RATE)
            print("Mega found!")

        elif "Uno" in p.description:
            uno_port = serial.Serial(p.device, BAUD_RATE)
            print("Uno found!")

        elif "Mode" in p.description:
            SKR_port = serial.Serial(p.device, BAUD_RATE)
            print("SKR found!")

# fetch DC motor commands
def get_DC_commands():
    DC_commands = input("DC Motor Commands:\n")
    DC_commands += '\n'
    return DC_commands

# fetch linear actuator commands
def get_LA_commands():
    LA_commands = input("Linear Actuator Commands:\n")
    LA_commands += '\n'
    return LA_commands

# fetch stepper motor commands
def get_stepper_commands():
    stepper_commands = input("Stepper Motor Commands:\n")
    stepper_commands += '\n'
    return stepper_commands

# main
if __name__ == '__main__':
    initialize_ports()

    # while (1):
        # grab input for DC motors and send to Mega
        # DC_commands = get_DC_commands()
        # mega_port.write(DC_commands.encode())
        # mega_echo = mega_port.readline()
        # print(mega_echo)
  
        # grab input for linear actuators and send to Uno
        # LA_commands = get_LA_commands()
        # uno_port.write(LA_commands.encode())
        # uno_echo = uno_port.readline()
        # print(uno_echo)  
  
        # grab input for stepper motors and send to SKR
        # stepper_commands = get_stepper_commands()
        # SKR_port.write(stepper_commands.encode())
        # SKR_echo = SKR_port.readline()
        # print(SKR_echo)
  
  
  
