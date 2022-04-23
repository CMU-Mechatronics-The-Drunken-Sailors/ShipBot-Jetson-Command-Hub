# sends new stepper motor positions to the SKR

from os import waitid
import time
import numpy as np
import serial
import sys
from . import initialization as init

old_x = 0
old_y = 0
old_z = 0

TIME_PAUSE = 0.5
def calcMoveTime(x, y, z):
    times = []
    amax = 100
    for new, orig, vmax in zip([x, y, z], [old_x, old_y, old_z], [16, 16, 16]):
        d = abs(new - orig) + 1e-6
        t = np.sqrt(4 * d / amax)
        if 2 * d / t > vmax:
            t = (d + vmax * vmax / amax) / vmax
        times.append(t)
    return max(times) + TIME_PAUSE

# homes the axes
def home_SKR():
    global old_x, old_y, old_z

    # set_stepper_motors("M502")
    # time.sleep(5)
    # print("Reset done!")

    start_time = time.time()

    set_stepper_motors("G92 X0 Y0 Z0", dont_wait_for_echo=True)
    send_SKR_command(x_pos=15, y_pos=15, z_pos=15, dont_wait_for_echo=True)
    print("Moved axes forward a bit before homing")

    command = "G28"
    set_stepper_motors(command, wait_for_ok=True)

    time.sleep(max(0, 45 - (time.time() - start_time))) # In case 'ok' was returned early, just wait min 30 seconds
    print("Homing done!")

    old_x = 0
    old_y = 0
    old_z = 0


# sets X/Y positions for gantry and Z position for end-effector
# arguments are optional
def send_SKR_command(x_pos = None, y_pos = None, z_pos = None, dont_wait_for_echo=False):
    global old_x, old_y, old_z

    command = "G1"

    new_x = x_pos if x_pos is not None else old_x
    new_y = y_pos if y_pos is not None else old_y
    new_z = z_pos if z_pos is not None else old_z
    
    if x_pos != None:
        command += " X" + str(x_pos)
    if y_pos != None:
        command += " Y" + str(y_pos)
    if z_pos != None:
        command += " Z" + str(z_pos)
        
    print(command)
    set_stepper_motors(command, dont_wait_for_echo=dont_wait_for_echo)

    waiting_time = calcMoveTime(new_x, new_y, new_z)
    print(f"Waiting for {waiting_time} seconds")
    time.sleep(waiting_time)

    old_x = new_x
    old_y = new_y
    old_z = new_z


    
# send to SKR
def set_stepper_motors(stepper_commands, wait_for_ok=False, dont_wait_for_echo=False):
    stepper_commands += '\n'
    init.SKR_port.flush()
    init.SKR_port.write(stepper_commands.encode())
    if not dont_wait_for_echo:
        if wait_for_ok:
            SKR_echo = ""
            while("ok" not in SKR_echo):
                SKR_echo = str(init.SKR_port.readline())
                print(SKR_echo)
        else:
            # Just wait for the first thing we get back
            SKR_echo = str(init.SKR_port.readline())
            print(SKR_echo)
  
