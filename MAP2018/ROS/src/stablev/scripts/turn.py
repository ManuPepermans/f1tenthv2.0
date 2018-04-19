#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from std_msgs.msg import Int32

# initial values and publishers
distances = ()
pub = rospy.Publisher('cornerOrWall', Float32, queue_size=10)
pub2 = rospy.Publisher('dontSeeCorner', Int32, queue_size=10)
stuck = 0
left = False
right = False
min_distance = 1.0
threshold = 0.03
threshold2 = 2.0

# get LiDAR data at given angle
def getRange(data, theta):
    index = int(theta / math.degrees(data.angle_increment))
    return data.ranges[index]

# check if car is making a turn 
def stopTurn(data):
    global cornering
    if data.data == 0:
        cornering = True
    elif data.data == 1:
        cornering = False

# check if the car needs to slow down
# check if there is enough space to make a turn, if there is no space publish neutral
# turning in two steps : backwards untill the car is parallel to the wall that was in front of the car
# forwards untill the car is parallel to the wall next to the car
def Lidar_data(data):
    global left,right,distances,stuck
    distances = data.ranges[517:562] #distance to 1.5m
    distances2 = data.ranges[528:552] #distance to 3m
    theta = 30
    range_right = getRange(data, 45)
    curr_range_right = getRange(data, 45 + theta)
    range_left = getRange(data, 225)
    curr_range_left = getRange(data, 225 - theta)
    thetaR = math.cos(math.radians(theta))
    max_distance_right = range_right / thetaR
    max_distance_left = range_left / thetaR

    print("stuck {}: ".format(stuck))

    if cornering == False:
        if stuck == 2:
            if left == True:
                if curr_range_right < max_distance_right + threshold and curr_range_right > max_distance_right - threshold:  # parallel to wall right
                    left = False
                    right = False
                    stuck = 0
                    pub.publish(9000)  # wall algorithm
                    pub2.publish(0)
            if right == True:
                if curr_range_left < max_distance_left + threshold and curr_range_left > max_distance_left - threshold:  # parallel to wall left
                    left = False
                    right = False
                    stuck = 0
                    pub.publish(9000)  # wall algorithm
                    pub2.publish(0)
        elif stuck == 1:
            print("range left: {}".format(range_left))
            print("range right: {}".format(range_right))
            if left == True:
                print("diff: {}".format(range_right - range_left))
                if curr_range_left < max_distance_left + threshold and curr_range_left > max_distance_left - threshold and range_right - range_left > threshold2: #parallel to wall left and wall right is more than 2 meter further than wall left
                    pub.publish(9700) # forwards right
                    pub2.publish(1)
                    stuck = 2
            elif right == True:
                print("diff: {}".format(range_left - range_right))
                if curr_range_right < max_distance_right + threshold and curr_range_right > max_distance_right - threshold and range_left - range_right > threshold2: # parallel to wall right and wall left is more than 2 meter further than well right
                    pub.publish(9800) # forwards left
                    pub2.publish(1)
                    stuck = 2
        elif stuck == 0:
            i = 0
            while i < (len(distances) - 1):
                if distances[i] <= 1.7:  # object at 1.7m or closer
                    if range_right > min_distance or range_left > min_distance:
                        if range_left > range_right:
                            left = True
                            pub.publish(9500)# backwards left
                            pub2.publish(1)
                            stuck = 1
                            i = 9000
                        else:
                            right = True
                            pub.publish(9600)# backwards right
                            pub2.publish(1)
                            stuck = 1
                            i = 9000
                    else:
                        pub.publish(9900) #neutral; stop moving
                        pub2.publish(1)
                        print("Can't turn, stopping!")
                elif i < (len(distances2) - 1):
                    if distances2[i] <= 2.3: # slow down
                        pub.publish(10000)
                        pub2.publish(1)
                        print("Slowing down")
                i += 5

if __name__ == '__main__':
    print('turn started')
    cornering = False
    rospy.init_node('turn_node', anonymous=True)
    rospy.Subscriber('scan', LaserScan, Lidar_data)
    rospy.Subscriber('TakingCorner', Int32, stopTurn)
    rospy.spin()
