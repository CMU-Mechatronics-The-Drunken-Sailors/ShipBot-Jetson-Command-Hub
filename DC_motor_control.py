# sends new DC motor speeds to the Mega

import serial
import sys
import initialization as init

# get encoder ticks from Mega
# returns array of ints - M1 M2 M3 M4
def get_encoder_ticks():
    encoder_request = "E\n"
    
    # read from Mega
    init.mega_port.write(encoder_request.encode())
    mega_echo = init.mega_port.readline()
    
    # parse encoder ticks
    encoder_ticks = []
    for ticks in mega_echo.split():
        try:
            encoder_ticks.append(int(ticks))
        except ValueError():
            pass

    # print(encoder_ticks)
    return encoder_ticks

# send motor speeds to Mega
# accepts series of ints - M1 M2 M3 M4
def set_DC_motors(M1_speed, M2_speed, M3_speed, M4_speed):
    # format speeds into a string
    int_list = [M1_speed, M2_speed, M3_speed, M4_speed]
    string_list = [str(val) for val in int_list]
    empty_string  = " "
    DC_commands = empty_string.join(string_list)
    DC_commands += '\n'
    # print(DC_commands)
    
    # send to Mega
    init.mega_port.write(DC_commands.encode())
    mega_echo = init.mega_port.readline()
    print(mega_echo)
