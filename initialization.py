# establishes USB port connections between Jetson and peripheral devices (Mega, Uno, SKR, RealSense)

import serial
import serial.tools.list_ports
import sys
import pyrealsense2 as rs

BAUD_RATE = 115200
mega_port = None
uno_port = None
SKR_port = None
pipeline = None

# opens and returns serial ports to connect to Mega, Uno, and SKR
def initialize_ports():
    global mega_port, uno_port, SKR_port
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

# opens and returns the camera pipeline
def initialize_camera():
    global pipeline

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
            # s.set_option(rs.option.enable_auto_white_balance, False) # NOT WORKING
            break
    if not found_rgb:
        print("The demo requires Depth camera with Color sensor")
        return None

    # enable depth image streaming
    config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 15)

    # enable color image streaming
    if device_product_line == 'L500':
        config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 15)
    else:
        config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 15)

    device.sensors[1].set_option(rs.option.white_balance, 3600) # 2800-6500/10 [4600]
    device.sensors[1].set_option(rs.option.saturation, 66) # 0-100/1 [64]
    device.sensors[1].set_option(rs.option.hue, 25) # -180-180/1 [0]
    device.sensors[1].set_option(rs.option.exposure, 600) # 1-10000/1 [166]

    # start streaming
    pipeline.start(config)
