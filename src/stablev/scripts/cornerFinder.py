#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from std_msgs.msg import Int32

# Global variables and Publishers
pub = rospy.Publisher('cornerOrWall', Float32, queue_size=10)
pub2 = rospy.Publisher('TakingCorner', Int32, queue_size=10)
path = [2,1,1,2] # path : 0 = straight, 1 = right, 2 = left
i = 0

# Gets LiDAR data 
def getRange(data, theta):
    index = int(theta / math.degrees(data.angle_increment))
    return data.ranges[index]

# Stops looking for a corner on data from the turnAround node
def stopCorner(data):
    global stopSearching
    if data.data == 0:
        stopSearching = False
    elif data.data == 1:
        stopSearching = True

# Returns the state from both walls.
# If the state is 'corner', right is 1 and left is 1. There is a corner on the left and right side.
# If the state is 'wall', right is 1 and left is 0. There is a wall on the right and a corner on the left.
def getState(data):
    global state, prev_state, left, right, prev_left, prev_right
    theta = 35
    range_right = getRange(data, 45)
    curr_range_right = getRange(data, 45 + theta)
    range_left = getRange(data, 225)
    curr_range_left = getRange(data, 225 - theta)

    thetaR = math.cos(math.radians(theta))
    max_distance_right = range_right / thetaR
    max_distance_left = range_left / thetaR

    threshold = (range_left + range_right) / 2.4
    threshold2 = threshold/35
    if curr_range_right > max_distance_right + threshold:
        prev_state = state
        state = 'corner'
        prev_right = right
        right = 1
        if curr_range_left > max_distance_left + threshold:
            prev_left = left
            left = 1
        elif curr_range_left < max_distance_left + threshold2 and curr_range_left > max_distance_left - threshold2:
            prev_left = left
            left = 0
    elif curr_range_right < max_distance_right + threshold2 and curr_range_right > max_distance_right - threshold2:
        prev_state = state
        state = 'wall'
        prev_right = right
        right = 1
        if curr_range_left > max_distance_left + threshold:
            prev_left = left
            left = 0
        elif curr_range_left < max_distance_left + threshold2 and curr_range_left > max_distance_left - threshold2:
            prev_left = left
            left = 1
    print("state: {}".format(state))
    print("L: {}".format(left))

# Checks if the detected corner is in the defined array (global variable), if so, the wheels need to be turned.
def pathChecker():
    global i, turnTo
    if i < (len(path)):
        if path[i] == 0:
            turnTo = 0
            pub.publish(5)
            print("straight")
            i += 1
        elif path[i] == 1 and right == 1 and state != 'wall':
            turnTo = 1
            pub.publish(40)
            pub2.publish(0)
            print("right")
            i += 1
        elif path[i] == 2 and left == 1 or (state == 'wall' and left == 0 and path[i] == 2):
            turnTo = 2
            pub.publish(-35)
            pub2.publish(0)
            print("left")
            i += 1
    else:
        turnTo = 0
        print("stop")
    print(i)

def process_scan(scan_data):
    global state, prev_state, left, right, prev_left, prev_right, keepTurned, turnTo
    getState(scan_data)

    if stopSearching == False:
        if prev_left is not left or prev_state is not state:
            if keepTurned is False:     # When the wheels aren't turned
                if state is 'corner':   # right will always be 1
                    pathChecker()       # doesn't matter if left or right is 1 => check path
                    keepTurned = True
                elif state is 'wall':     # right will always be 1
                    if left is 0:
                        pathChecker()
                        keepTurned = True
                    elif left is 1:
                        pub.publish(9000)
                        pub2.publish(1)
                        print("wall")
            elif keepTurned is True:    # If the wheels are turned, change mode on the value of some parameters
                if state is 'wall':
                    if left is 1 and turnTo is 2:
                        turnTo = 0
                        keepTurned = False
                        pub.publish(9000)
                        pub2.publish(1)
                        print("wall left")
                    elif right is 1 and turnTo is 1:
                        turnTo = 0
                        keepTurned = False
                        pub.publish(9000)
                        pub2.publish(1)
                        print("wall right")
                    elif turnTo is 0:
                        turnTo = 0
                        keepTurned = False
                        pub.publish(9000)
                        pub2.publish(1)
                elif state is 'corner':
                    if left is 0 and turnTo is 2:
                        turnTo = 0
                        keepTurned = False
                        pub.publish(9000)
                        pub2.publish(1)
                        print("wall left")
                    elif turnTo is 0:
                        turnTo = 0
                        keepTurned = False
                        pub.publish(9000)
                        pub2.publish(1)


if __name__ == '__main__':
    print('corner finding started')
    rospy.init_node('corner_finder', anonymous=True)
    state = 'wall'
    prev_state = state
    right = 1
    prev_right = right
    left = 1
    prev_left = left
    keepTurned = False
    stopSearching = False
    turnTo = 0  # 0 = nothing, 1 = right, 2 = left
    rospy.Subscriber('scan', LaserScan, process_scan)
    rospy.Subscriber('dontSeeCorner', Int32, stopCorner)
    rospy.spin()
