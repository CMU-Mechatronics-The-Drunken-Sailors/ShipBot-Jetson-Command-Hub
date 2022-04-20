# parses mission file and returns list of tuples denoting tasks in order
#
# tuples of three elements are valves: (station, valve-number, valve-position)
# tuples of four elements are breakers: (station, breaker-box, breaker-number, breaker-position)
#
# station is A-H
# valve-number is 1, 2, or 3
# valve-position is 0-360 if valve-number is 1 or 2, or 0 (open) and 1 (closed) if valve-number is 3
# breaker-box is A or B
# breaker-number is 1, 2, or 3
# breaker-position is U (up) or D (down)
#
# final value in the mission text is target completion time; we can ignore this and just go as fast as possible

import sys

# returns list of tuples denoting tasks in order
def read_mission_file():
  # open file and return text
  filename = input("What is the mission file?\n")
  file = open(filename, "r")
  mission_file = file.read()
  
  # parse text into a list of tasks
  parsed_mission_file = mission_file.split(",")
  
  mission_tasks = []
  for task_string in parsed_mission_file:
    # if we reached the completion time, then we're done parsing tasks
    task_string = task_string.lstrip()
    if not task_string[0].isalpha(): break
    
    # set station letter
    station = task_string[0]
    
    # check if we are dealing with a valve
    valve_num = 0 # 1, 2, or 3
    valve_pos = 0 # 0-360 or 0/1
    
    if 'V1' in task_string:
      valve_num = 1
      valve_pos = int(task_string[task_string.find(" ")+1 : len(task_string)]) # get angle
      
    if 'V2' in task_string:
      valve_num = 2
      valve_pos = int(task_string[task_string.find(" ")+1 : len(task_string)]) # get angle
      
    if 'V3' in task_string:
      valve_num = 3
      valve_pos = int(task_string[task_string.find(" ")+1 : len(task_string)]) # get angle
      
    # check if we are dealing with a breaker
    breaker_box = '0' # 'A' or 'B'
    breaker_num = 0 # 1, 2, or 3
    breaker_pos = '0' # 'U' or 'D'
    
    if 'B1' in task_string:
      breaker_box = task_string[1]
      breaker_num = 1
      breaker_pos = task_string[6]
      
    if 'B2' in task_string:
      breaker_box = task_string[1]
      breaker_num = 2
      breaker_pos = task_string[6]
      
    if 'B3' in task_string:
      breaker_box = task_string[1]
      breaker_num = 3
      breaker_pos = task_string[6]
      
    # add the task to our list
    if valve_num != 0:
      task_tuple = (station, valve_num, valve_pos) # we have a valve task
    elif breaker_num != 0:
      task_tuple = (station, breaker_box, breaker_num, breaker_pos) # we have a breaker task
    
    mission_tasks.append(task_tuple)
  
  return mission_tasks
