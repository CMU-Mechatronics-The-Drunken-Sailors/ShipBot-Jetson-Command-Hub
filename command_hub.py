# command hub for Jetson Xavier NX
# communicates with Uno, Mega, and SKR boards
# for Mega, sends command of 4 values indicating velocity for each DC motor (deg/sec)
# for Uno, sends command of 3 values indicating direction of linear actuators (forward, back, stop)
# for SKR, sends command of N values indicating stepper motor velocity

import serial
import sys

# open ports - how to automate port assignment?
mega_port = serial.Serial('/dev/ttyACM0', '115200')
# uno_port = serial.Serial('/dev/ttyACM1', '115200')
# SKR_port = serial.Serial('/dev/ttyACM2', '115200')

while (1):
  # grab input for DC motors and send to Mega
  DC_motor_commands = input("DC Motor Commands")
  print(DC_motor_commands)
  mega_port.write(DC_motor_commands)
  
  # grab input for linear actuators and send to Uno
  linear_actuator_commands = input("Linear Actuator Commands")
  print(linear_motor_commands)
#   uno_port.write(linear_motor_commands)
  
  # grab input for stepper motors and send to SKR
  stepper_motor_commands = input("Stepper Motor Commands")
  print(stepper_motor_commands)
#   SKR_port.write(stepper_motor_commands)
  
  
  
  
