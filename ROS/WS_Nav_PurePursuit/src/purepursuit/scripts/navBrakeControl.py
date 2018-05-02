#!/usr/bin/env python
#
# Copyright (c) 2018, University of Antwerp.
# All rights reserved.
#
# Jens de Hoog, Stevie Maes, Bernd Smits, Jonas Vercauteren

import rospy
import curses

from std_msgs.msg import Float32
from std_msgs.msg import String

# initial values for finite state machines
rpm = 0
rpmC = True  #Checks if the RPM was whitin the rpm-range 1.1(foward)&1.1(backwards) during braking
Brake = "NoBrake"
inBrake = False

# pubBrake node is
#   - Publishing to the brake topic
#   - The message type is String
#   - The queue has a size '10' which describes the limited amount of queued messages
pubBrake = rospy.Publisher('brake', String, queue_size=10)

# Get input from the emergency topic to brake with keyboard input
def emergency(data):
    global emergencyState
    emergencyState = "Brake"
    print("emergency")
    braking()

# read rpm data and check if rpm is low enough during braking
def RpmData(data):
    global rpm,rpmC,Brake,emergencyState
    rpm = data.data
    if emergencyState == "Brake" and rpm < 1.1:
        print("rpmC is false ")
        rpmC = False
        braking()
    if emergencyState == "Deny" and rpmC == False:
        print("rpmC is true")
        rpmC = True
        braking()

# finite state machine to check if the car needs to brake and when to stop braking
def braking():
    global inBrake,Brake,rpmC,rpm

    # If the car isn't braking
    if inBrake == False:
        # If the emergencyState == "Brake"
        if emergencyState == "Brake" and rpmC == False:
            inBrake = True
            Brake = "Brake"
            pubBra.publish(Brake)
            rospy.loginfo(Brake)
        elif emergencyState == "Deny" or rpmC == True:
            Brake = "NoBrake"
            pubBra.publish(Brake)
            rospy.loginfo(Brake)

    # If the car is braking
    elif inBrake == True:
        if emergencyState == "Brake" and rpmC == False:
            Brake = "Brake"
            pubBra.publish(Brake)
            rospy.loginfo(Brake)
        elif emergencyState == "Brake" and rpmC == True:
            inBrake = False
            Brake = "NoBrake"
            pubBra.publish(Brake)
            rospy.loginfo(Brake)

if __name__ == '__main__':
    rospy.init_node('navBrakeControlNode', anonymous=True)
    # Subscribing to emergency to receive String data which will trigger the emergency function
    rospy.Subscriber("emergency", String, emergency)
    # Subscribing to RPMcounter to receive Float32 data which will trigger the RpmData function
    rospy.Subscriber("RPMCounter", Float32, RpmData)
    rospy.spin()