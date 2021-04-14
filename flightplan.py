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

# Take off and up to 6 feet 72 inches
# Take off default is 32 inches
drone.connect()
drone.takeoff()
# Go up 40 inches to get to 6 feet
# Convert everything to centimeters
drone.move_up(102)

# Go east (forward) 5 feet and turn north (left)
# stay at 6 feet
drone.move_forward(152)
drone.rotate_counter_clockwise(90)

# Go north (forward) 6 feet and turn east (right)
# stay at 6 feet
drone.move_forward(183)
drone.rotate_clockwise(90)

# drop to 3 feet
# go east (forward) 3 and turn south (right)
drone.move_down(91)
drone.move_forward(91)
drone.rotate_clockwise(90)

# go up to 4 feet
# go south (forward) 3 and turn east (left)
drone.move_up(30)
drone.move_forward(91)
drone.rotate_counter_clockwise(90)

# stay at 4 feet
# go east (forward) 6 feet
drone.move_forward(183)

# Land the drone
drone.land()
