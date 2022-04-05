# command hub for Jetson Xavier NX
# communicates with Uno, Mega, and SKR boards
# for Mega, sends command of 4 values indicating velocity for each DC motor (deg/sec)
# for Uno, sends command of 3 values indicating direction of linear actuators (forward, back, stop)
# for SKR, sends command of N values indicating stepper motor velocity

import serial
import sys
import time

# open ports - how to automate port assignment? see: https://stackoverflow.com/questions/24214643/python-to-automatically-select-serial-ports-for-arduino
mega_port = serial.Serial('/dev/ttyACM0', '115200')
# uno_port = serial.Serial('/dev/ttyACM1', '115200')
# SKR_port = serial.Serial('/dev/ttyACM2', '115200')

serial_wait = 0.5

while (1):
  # grab input for DC motors and send to Mega
  DC_motor_commands = input("DC Motor Commands:\n")
  mega_port.write(bytes(DC_motor_commands, 'utf-8'))
  time.sleep(serial_wait)
  mega_echo = mega_port.readline()
  print(mega_echo)
  
  # grab input for linear actuators and send to Uno
  #linear_actuator_commands = input("Linear Actuator Commands:\n")
  #uno_port.write(linear_actuator_commands.encode())
  #uno_echo = uno_port.readline()
  #print(uno_echo)  
  
  # grab input for stepper motors and send to SKR
  # stepper_motor_commands = input("Stepper Motor Commands")
  # print("Sent: " + stepper_motor_commands)
#   SKR_port.write(stepper_motor_commands)
  
  
  
  
