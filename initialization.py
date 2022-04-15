# establishes USB port connections between Jetson and peripheral devices (Mega, Uno, SKR, RealSense)

import serial
import serial.tools.list_ports
import sys

BAUD_RATE = 115200

# open ports
def initialize_ports():
    mega_port = uno_port = SKR_port = None
    ports = list(serial.tools.list_ports.comports())
    
    for p in ports:
        print(p)

        if "Mega" in p.description:
            mega_port = serial.Serial(p.device, BAUD_RATE)
            print("Mega found!")

        elif "Uno" in p.description:
            uno_port = serial.Serial(p.device, BAUD_RATE)
            print("Uno found!")

        elif "Mode" in p.description:
            SKR_port = serial.Serial(p.device, BAUD_RATE)
            print("SKR found!")

    return (mega_port, uno_port, SKR_port)
