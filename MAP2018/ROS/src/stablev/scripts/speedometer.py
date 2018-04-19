#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float32 #import RPMCounter

pub = rospy.Publisher('speedometer', Float32, queue_size=1)

def callback(data):
    rpm = data.data #Read data from RPMCounter
    # the two gears from the spur gear to the differential of the wheel are 13teeth and 37teeth
    speed = (rpm*13)/37 # Amount of rotations the wheel makes
    speed = (speed * 0.297) / 0.1
    #print("Speed: {}".format(speed * 3.6))
    pub.publish(speed)

if __name__ == '__main__':
    print("Speedometer")
    rospy.init_node('speedometer', anonymous=True)
    rospy.Subscriber('RPMCounter', Float32, callback)
    rospy.spin()