# sends new DC motor speeds to the Mega

import serial
import sys

# get encoder ticks from Mega
# returns array of ints - M1 M2 M3 M4
def get_encoder_ticks(mega_port):
    encoder_request = "E\n"
    
    # read from Mega
    mega_port.write(encoder_request.encode())
    mega_echo = mega_port.readline()
    
    # parse encoder ticks
    encoder_ticks = []
    for ticks in mega_echo.split()
        try:
            encoder_ticks.append(int(ticks))
        except ValueError():
            pass
    
    return encoder_ticks

# send motor speeds to Mega
# accepts series of ints - M1 M2 M3 M4
def set_DC_motors(mega_port, M1_speed, M2_speed, M3_speed, M4_speed):
    speeds = [M1_speed, M2_speed, M3_speed, M4_speed]
    
    # format speeds to a string
    DC_commands = " "
    DC_commands.joint(speeds)
    DC_commands += '\n'
    
    # send to Mega
    mega_port.write(DC_commands.encode())
    mega_echo = mega_port.readline()
    print(mega_echo)
