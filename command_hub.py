# command hub for Jetson Nano
# communicates with Mega, Uno, and SKR boards
# for Mega, sends command of 4 values indicating velocity for each DC motor (deg/sec per motor)
# for Uno, sends command of 2 values indicating direction of linear actuators (pair and solo LAs)
# for SKR, sends command of 3 values indicating stepper motor positions (X, Y, Z)

import initialization as init
import DC_motor_control as Mega
import linear_actuator_control as Uno
import stepper_motor_control as SKR

# user input for testing/debugging
def manual_control():
    while (1):
        # send DC motor commands to Mega
        DC_commands = input("DC Motor Commands:\n")
        if DC_commands != '':
            DC_commands += '\n'
            init.mega_port.write(DC_commands.encode())
            mega_echo = init.mega_port.readline()
            print(mega_echo)
  
        # send linear actuators commands to Uno
        LA_commands = input("Linear Actuator Commands:\n") # user input for testing/debugging
        if LA_commands != '':
            if LA_commands == 'RR':
                Uno.retract_pair_retract_solo()
            elif LA_commands == 'RE':
                Uno.retract_pair_extend_solo()
            elif LA_commands == 'ER':
                Uno.extend_pair_retract_solo()
            elif LA_commands == 'EE':
                Uno.extend_pair_extend_solo()
  
        # send stepper motor commands to SKR
        # stepper_commands = input("Stepper Motor Commands:\n") # user input for testing/debugging
        # if stepper_commands == '':
        #     return
        # else:
        #     SKR.set_stepper_motors(SKR_port, stepper_commands)

if __name__ == '__main__':
    # open USB ports
    init.initialize_ports()
    init.initialize_camera()

    # manual_control()

    # test DC functions
    # Mega.set_DC_motors(0, 0, 0, 0)
    # encoder_ticks = Mega.get_encoder_ticks()
