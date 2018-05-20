#!/usr/bin/env python
#
# Copyright (c) 2018, University of Antwerp.
# All rights reserved.
#
# Jens de Hoog, Stevie Maes, Bernd Smits, Jonas Vercauteren

import rospy
import curses
import math

from std_msgs.msg import Float32
from geometry_msgs.msg import PoseWithCovarianceStamped

#Initial values
newS = 0
newNS = 0
newX = 0
newY = 0
prevS = 0
prevNS = 0
prevX = 0
prevY = 0

# pubVel node is
#   - Publishing to the velocity topic
#   - The message type is Float32
#   - The queue has a size '10' which describes the limited amount of queued messages
pubVelocity = rospy.Publisher('velocity', Float32, queue_size=10)

def velocityCal(data):
    global newS, newNS, newX, newY, prevS, prevNS, prevX, prevY
    # Get new values
    newS = data.header.stamp.secs
    newNS = data.header.stamp.nsecs
    newX = data.pose.pose.position.x
    newY = data.pose.pose.position.y

    # Get difference compared to previous values
    diffS = newS - prevS
    diffNS = newNS - prevNS
    diffX = newX - prevX
    diffY = newY - prevY
    
    # Set new values as previous
    prevS = newS
    prevNS = newNS
    prevX = newX
    prevY = newY

    # Calculate Traversed distance and time
    distanceTrav = ((diffX**2)+(diffY**2))**(.5)
    distanceSec = float(diffS)+(float(diffNS)/1000000000)


    # Calculate velocity based on traversed distance and time
    velocity = distanceTrav/distanceSec
    pubVelocity.publish(velocity)
    rospy.loginfo(velocity)

if __name__ == '__main__':
    rospy.init_node('velocity', anonymous=True)
    # Subscribing to amcl_pose to receive PoseWithCovarianceStamped data which will trigger the velocityCal function
    rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, velocityCal)
    rospy.spin()
