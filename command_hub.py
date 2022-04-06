# command hub for Jetson Nano
# communicates with Mega, Uno, and SKR boards
# for Mega, sends command of 4 values indicating velocity for each DC motor (deg/sec per motor)
# for Uno, sends command of 2 values indicating direction of linear actuators (pair and solo LAs)
# for SKR, sends command of 3 values indicating stepper motor positions (X, Y, Z)

import serial
import sys

# open ports - how to automate port assignment? see: https://stackoverflow.com/questions/24214643/python-to-automatically-select-serial-ports-for-arduino
mega_port = serial.Serial('/dev/ttyACM0', '115200')
uno_port = serial.Serial('/dev/ttyACM1', '115200')
# SKR_port = serial.Serial('/dev/ttyACM3', '115200')

while (1):
  # grab input for DC motors and send to Mega
  DC_motor_commands = input("DC Motor Commands:\n")
  DC_motor_commands += '\n'
  mega_port.write(DC_motor_commands.encode())
  # mega_echo = mega_port.readline()
  # print(mega_echo)
  
  # grab input for linear actuators and send to Uno
  linear_actuator_commands = input("Linear Actuator Commands:\n")
  linear_actuator_commands += '\n'
  uno_port.write(linear_actuator_commands.encode())
  # uno_echo = uno_port.readline()
  # print(uno_echo)  
  
  # grab input for stepper motors and send to SKR
  # stepper_motor_commands = input("Stepper Motor Commands:\n")
  # stepper_motor_commands += '\n'
  # SKR_port.write(stepper_motor_commands.encode())
  # SKR_echo = SKR_port.readline()
  # print(SKR_echo)
  
  
  
