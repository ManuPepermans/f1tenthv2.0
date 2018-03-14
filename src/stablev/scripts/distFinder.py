#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Float32

# standaard message for laserscan
from sensor_msgs.msg import LaserScan

# initial values for finite state machines
inRange = False
inBrake = False
Brake = "NoBrake"
dist = "clear"
distances = ()
rpm = 0
rpmC = True

pubObs = rospy.Publisher('obstruction', String, queue_size=10)
pubBra = rospy.Publisher('brake', String, queue_size=10)

# get input from emergency node to brake with keyboard input
def emergency(data):
    global dist
    dist = "obs"
    print("emergency")
    braking()

# read lidar data, 504-574 lidar data 1 meter in front of the car
def LidarData(data):
    global distances
    distances = data.ranges[504:574]
    obstruction()

# read rpm data and check if rpm is low enough during braking
def RpmData(data): 
    global rpm,rpmC,dist,Brake
    rpm = data.data
    if Brake == "brake" and rpm < 1.1:
        print("rpmC is false ")
        rpmC = False
        braking()
    if dist == "clear" and rpmC == False:
        print("ready for brake")
        rpmC = True
        braking()

# finite state machine to check if there is an obstacle
def obstruction():
    global dist, distances,inRange
    i = 0
    if inRange == False:
        tempInRange = False
        while i < (len(distances)-1):
            if distances[i] <= 1: 
                tempInRange = True
            i += 5
        if tempInRange == True:
            inRange = True
            dist = "obs"
            braking()
            pubObs.publish(dist)
            print(dist)
    elif inRange == True:
        tempInRange = False
        while i < (len(distances)-1):
            if distances[i] <= 1: 
                tempInRange = True
            i += 5
        if tempInRange == False:
            inRange = False
            dist = "clear"
            braking()
            pubObs.publish(dist)
            print(dist)


# finite state machine to check if the car needs to brake and when to stop braking
def braking():
    global inBrake,Brake,rpmC,rpm
    print("brake function")
    if inBrake == False:
        tempInRange = False
        if dist == "clear" or rpmC == False: 
            tempInRange = True
        if tempInRange == True:
            inBrake= True
            Brake = "NoBrake"
            pubBra.publish(Brake)
            print(Brake)
    elif inBrake == True:
        tempInRange = False
        if dist == "obs" and rpm > 0.5:
            tempInRange = True
        if tempInRange == True:
            inBrake = False
            Brake = "brake"
            pubBra.publish(Brake)
            print(Brake)

if __name__ == '__main__':
    print("DistFinder node started")
    rospy.init_node('distfinder', anonymous = True)
    pubObs.publish(dist)
    braking()
    rospy.Subscriber("emergency",String,emergency)
# laser data from scan ->
    rospy.Subscriber("scan", LaserScan, LidarData)
    rospy.Subscriber("RPMCounter",Float32,RpmData)
    rospy.spin()
