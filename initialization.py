# establishes USB port connections between Jetson and peripheral devices (Mega, Uno, SKR, RealSense)

import serial
import serial.tools.list_ports
import sys
import pyrealsense2.pyrealsense2 as rs

BAUD_RATE = 115200

# opens and returns serial ports to connect to Mega, Uno, and SKR
def initialize_ports():
    mega_port = uno_port = SKR_port = None
    ports = list(serial.tools.list_ports.comports())
    
    # go thru open ports
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

# opens and returns the camera pipeline
def initialize_camera():
     # configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()

    # get device product line for setting a supporting resolution
    pipeline_wrapper = rs.pipeline_wrapper(pipeline)
    pipeline_profile = config.resolve(pipeline_wrapper)
    device = pipeline_profile.get_device()
    device_product_line = str(device.get_info(rs.camera_info.product_line))

    # Check if the camera has RGB color channels set up
    found_rgb = False
    for s in device.sensors:
        if s.get_info(rs.camera_info.name) == 'RGB Camera':
            found_rgb = True
            break
    if not found_rgb:
        print("The demo requires Depth camera with Color sensor")
        return None

    # enable depth image streaming
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)

    # enable color image streaming
    if device_product_line == 'L500':
        config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 15)
    else:
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 15)

    # start streaming
    pipeline.start(config)

    return pipeline
