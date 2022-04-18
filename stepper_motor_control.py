# sends new stepper motor positions to the SKR

import serial
import sys

# send to SKR
def set_stepper_motors(SKR_port, stepper_commands):
    stepper_commands += '\n'
    SKR_port.write(stepper_commands.encode())
    SKR_echo = SKR_port.readline()
    print(SKR_echo)
  
