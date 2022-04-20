# parses mission file and returns list of tuples denoting tasks in order
#
# tuples of two elements are valves: (valve-number, valve-position)
# tuples of three elements are breakers: (breaker-box, breaker-number, breaker-position)
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

# create station class
class station:
  def __init__(self, name):
    self.name = name
    self.task_type = '0' # 'V' for valve, 'B' for breaker
    self.task_list = []

# declare 8 stations, A-H
station_A = station('A')
station_B = station('B')
station_C = station('C')
station_D = station('D')
station_E = station('E')
station_F = station('F')
station_G = station('G')
station_H = station('H')

station_list = [station_A, station_B, station_C, station_D, station_E, station_F, station_G, station_H]

# returns list of tuples denoting tasks in order
def read_mission_file():
  global station_A, station_B, station_C, station_D, station_E, station_F, station_G, station_H

  # open file and return text
  filename = input("What is the mission file?\n")
  file = open("Command_Hub/mission_files/all_stations.txt", "r") # change this manually or set to filename for user input
  mission_file = file.read()
  
  # parse text into a list of tasks
  parsed_mission_file = mission_file.split(",")
  
  for task_string in parsed_mission_file:
    # if we reached the completion time, then we're done parsing tasks
    task_string = task_string.lstrip()
    if not task_string[0].isalpha(): break
    
    # identify station
    station_name = task_string[0]

    if station_name == 'A':
      current_station = station_A
    elif station_name == 'B':
      current_station = station_B
    elif station_name == 'C':
      current_station = station_C
    elif station_name == 'D':
      current_station = station_D
    elif station_name == 'E':
      current_station = station_E
    elif station_name == 'F':
      current_station = station_F
    elif station_name == 'G':
      current_station = station_G
    elif station_name == 'H':
      current_station = station_H
    
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
      # we have a valve_task
      current_station.task_type = 'V'
      task_tuple = (valve_num, valve_pos)
    elif breaker_num != 0:
      # we have a breaker task
      current_station.task_type = 'B'
      task_tuple = ( breaker_box, breaker_num, breaker_pos)

    # add task to appropriate station
    current_station.task_list.append(task_tuple)
