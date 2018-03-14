#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

pub = rospy.Publisher('speed', Float32, queue_size=10)
speedReached = False

def callback(data):
    global speed, speedReached
    measuredRPM = data.data
    #print("WantedRPM: {}".format(wantedRPM))
    #print("MeasuredRPM: {}".format(measuredRPM))
    #print("Speed: {}".format(speed))
    # If the wanted RPM is lower than the Measured RPM, we adjust the speed
    # For safety we also check if the speed has already been reached
    if wantedRPM > measuredRPM and speedReached is not True:
        # Speed threshold: 15 keyboard input
        if speed < 15:
            speed = speed + 0.1
        pub.publish(speed)
    # If the speed has been reached once, but we slow down, the speed can be set again
    elif wantedRPM < (measuredRPM - 2) and speedReached is True:
        speedReached = False
    else:
        speedReached = True

if __name__ == '__main__':
    rospy.init_node('SpeedControl', anonymous=True)
    # Gets a value from a launch file, can also be done with using input command from python-libraries.
    vel = rospy.get_param('~vel',5.0)
    wantedRPM = (vel / 3.6) * 0.1 / 0.297 * 37 / 13
    rospy.Subscriber('RPMCounter', Float32, callback)
    rospy.spin()
