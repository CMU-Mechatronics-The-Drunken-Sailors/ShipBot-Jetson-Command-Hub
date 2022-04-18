# Jetson-Command-Hub
Code for the Jetson board to send commands to other devices (Uno, Mega, SKR) as well as connect to RealSense camera

Basic driving commands:

Forwards - all wheels forward

Backwards - all wheels backward

Rotate Left - 2+4 backward, 1+3 forward

Rotate Right - 1+3 backward, 2+4 forward

Translate Right - 2+3 backward, 1+4 forward

Translate Left - 1+4 backward, 2+3 forward

Basic end-effector positions:

Arm is bent, tip is straight -> retract LA pair, retract solo LA -> -255 -255

Arm is bent, tip is bent -> retract LA pair, extend solo LA -> -255 255

Arm is straight, tip is straight -> extend LA pair, retract solo LA -> 255 -255

Arm is straight, tip is bent -> extend LA pair, extend solo LA -> 255 255
