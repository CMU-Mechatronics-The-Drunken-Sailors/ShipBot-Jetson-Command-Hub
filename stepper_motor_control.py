# sends new stepper motor positions to the SKR

import initialization

def get_stepper_commands():
    stepper_commands = input("Stepper Motor Commands:\n")
    stepper_commands += '\n'
    SKR_port.write(stepper_commands.encode())
    SKR_echo = SKR_port.readline()
    print(SKR_echo)
  
