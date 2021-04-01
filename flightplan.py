#!/usr/bin/env python3

# Rescue mission in the mountains
# All distances are 1:10 or 1 ft for every real 10 ft.
# So divide the instructions by 10
# i.e. 60 ft is really 60/10 or 6ft.

# if running locally, you need to install the djitello module
# run this on your linux or mac machine
# pip3 install djitello

# Install the module
from djitellopy import Tello

# Create our tello drone object
drone = Tello()

# Take off and up to 6 feet
drone.connect()
drone.takeoff()
drone.move_up(6)

# Go east (forward) 5 feet and turn north (left)
# stay at 6 feet
drone.move_forward(5)
drone.rotate_counter_clockwise(90)

# Go north (forward) 6 feet and turn east (right)
# stay at 6 feet
drone.move_forward(6)
drone.rotate_clockwise(90)

# drop to 3 feet
# go east (forward) 3 and turn south (right)
drone.move_down(3)
drone.move_forward(3)
drone.rotate_clockwise(90)

# go up to 4 feet
# go south (forward) 3 and turn east (left)
drone.move_up(1)
drone.move_forward(3)
drone.rotate_counter_clockwise(90)

# stay at 4 feet
# go east (forward) 6 feet
drone.move_forward(6)

# Land the drone
drone.land()