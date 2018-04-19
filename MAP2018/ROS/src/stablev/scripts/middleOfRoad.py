#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from race.msg import pid_input

# Global variables and publishers
vel = 0.0
pub = rospy.Publisher('error', pid_input, queue_size=10)

# Gets the right data from the LiDAR sensor
def getRange(data, theta):
    index = int(theta / math.degrees(data.angle_increment))
    return data.ranges[index]

# Changes speed, if value from speedControl is changed
def adjustSpeed(data):
    global vel
    vel = data.data

# Calculates the error the car is moved from the middle, this error and the speed from the car is sent to middleRoadControl
def callback(data):
    theta = 50
    a = getRange(data, 45 + theta)
    b = getRange(data, 45)
    a1 = getRange(data, 225- theta)
    b1 = getRange(data, 225)
    swing = math.radians(theta)

    alpha = math.atan2(a * math.cos(swing) - b, a * math.sin(swing))
    alpha1 = math.atan2(a1 * math.cos(swing) - b1, a1 * math.sin(swing))
    AB = b * math.cos(alpha)
    AB1 = b1 * math.cos(alpha1)

    AC = 1
    CD = AB + AC * math.sin(alpha)
    CD1 = AB1 + AC * math.sin(alpha1)
    middle = (CD + CD1) / 2
    error = CD - middle + (middle/10)

    msg = pid_input()
    msg.pid_error = error
    msg.pid_vel = vel
    pub.publish(msg)


if __name__ == '__main__':
    print("Middle Of Road Node Started")
    rospy.init_node('MiddleOfRoadNode', anonymous=True)
    rospy.Subscriber("scan", LaserScan, callback)
    rospy.Subscriber("speed", Float32, adjustSpeed)
    rospy.spin()

