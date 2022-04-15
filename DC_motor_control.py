# sends new DC motor speeds to the Mega

import initialization

def set_DC_motors():
    DC_commands = input("DC Motor Commands:\n")
    DC_commands += '\n'
    mega_port.write(DC_commands.encode())
    mega_echo = mega_port.readline()
    print(mega_echo)
