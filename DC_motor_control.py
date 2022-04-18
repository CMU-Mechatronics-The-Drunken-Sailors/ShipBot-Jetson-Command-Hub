# sends new DC motor speeds to the Mega

import serial
import sys

# get encoder ticks from Mega
def get_encoder_ticks(mega_port):
    encoder_request = "E\n"
    mega_port.write(encoder_request.encode())
    
    
    return ()

# send motor speeds to Mega
def set_DC_motors(mega_port, M1_speed, M2_speed, M3_speed, M4_speed):
    speeds = [M1_speed, M2_speed, M3_speed, M4_speed]
    
    # format ints to a string
    DC_commands = " "
    DC_commands.joint(speeds)
    DC_commands += '\n'
    
    # send to Mega
    mega_port.write(DC_commands.encode())
    mega_echo = mega_port.readline()
    print(mega_echo)
