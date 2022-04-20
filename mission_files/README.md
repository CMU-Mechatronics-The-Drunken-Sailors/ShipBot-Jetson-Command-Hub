Mission files provided by course staff - from the project specs:

The testbed has eight stations, whose Cartesian coordinates your team may have pre-stored. Stations are 
coded A through H.

There are 4 types of devices. These have codes assigned to them: 

Gate Valve: V1
 
• These valves may be oriented upwards or forwards, as seen in Figure 1. 

Large Valve: V2 

Stopcock Valve: V3 

• These valves may be oriented upwards or forwards, as seen in Figure 1. 

Breakers: B1, B2, B3 

• There are two breaker boxes: Box A has the ‘ON’ position at the top, and Box B has 
the ‘ON’ position at the bottom. The letter of the box (A or B) will be indicated after 
the station letter. On both boxes, it is easier to flip the switches from ‘ON’ to ‘OFF’. 

• Each breaker box has 3 breakers in the same configuration (one DS, two SS) labeled 
B1, B2, B3  from left to right. 
 
Each device has an indicator for actuation: 

• V1 and V2 will include a desired angle from 0-360 degrees, measured clockwise from the 12 
o’clock  position  on  each  valve  (i.e.,  3 o’clock  is  90  degrees).  The  12  o’clock  position  is 
represented as the position “directly ahead” using the analogy of a 12-hour clock, and is defined 
on each valve after the instructors have set that respective valve to its initial state. 

• Rotation of V1 and V2 by the robot can be in either the clockwise or counterclockwise direction 
to achieve the desired angle.

• V3 includes a desired position (open or closed), designated by 0=open and 1=closed.

• B1, B2, B3, if mentioned in the file, must be switched to the  ’up’ or ‘down’ position.
 
An example file: “AV1 175, CA B2 U, DV3 0, FB B3 U, GV2 50, 400”, indicating: 

• Turn gate valve at station A to 175 degrees clockwise from the 12 o’clock position 

• Breaker box A is at station C: ensure the second switch is up 

• Ensure stopcock valve at station D is open 

• Breaker box B is at station F: ensure the third switch up 

• Turn large valve at station G to 50 degrees clockwise from the 12 o’clock position 

• The target completion time is 400 seconds 
 
Another example: “BV3 1, CB B1 U, CB B2 D, EA B1 U, FV1 60, 370”, indicating: 

• Ensure stopcock valve at station B is closed 

• Breaker box B is at station C: ensure the first switch is up 

• Breaker box B is at station C: ensure the second switch is down 

• Breaker box A is at station E: ensure the first switch is up 

• Turn gate valve at station F to 60 degrees clockwise from the 12 o’clock position 

• The target completion time is 370 seconds 
 
Notes: The stations in the file may be provided in any order and may not be unique. The target completion 
time will always be the last value in the file. The text will be saved as one line, as shown in the examples 
above, in a .txt file delivered to the team on a flash drive.

You are allowed to adjust the order in which devices are visited to improve mission performance. However, 
if you choose to do this, the group must declare and have verified that they have built that capability into 
their mission planner prior to the demonstration. Otherwise, the expectation is that all operations will be 
completed in the exact order they are provided.
