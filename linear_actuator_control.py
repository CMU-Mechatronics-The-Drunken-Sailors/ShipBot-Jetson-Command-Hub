# sends new linear actuator commands to the Uno

import initialization

def set_LA_commands():
    LA_commands = input("Linear Actuator Commands:\n")
    LA_commands += '\n'
    uno_port.write(LA_commands.encode())
    uno_echo = uno_port.readline()
    print(uno_echo)  
