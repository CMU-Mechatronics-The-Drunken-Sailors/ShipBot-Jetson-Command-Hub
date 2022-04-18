# sends new DC motor speeds to the Mega

import serial
import sys

# send to Mega
def set_DC_motors(mega_port, DC_commands):
    DC_commands += '\n'
    mega_port.write(DC_commands.encode())
    mega_echo = mega_port.readline()
    print(mega_echo)
