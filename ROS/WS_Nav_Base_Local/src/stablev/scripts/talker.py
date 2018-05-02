#!/usr/bin/env python
#
# Copyright (c) 2018, University of Antwerp.
# All rights reserved.
#
# Jens de Hoog, Stevie Maes, Bernd Smits, Jonas Vercauteren

import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from race.msg import drive_param
from race.msg import drive_values

# initial values
input = drive_values()
input.pwm_angle = 9831.0
input.pwm_drive = 9831.0
brake = "NoBrake"

# pub node is
#   - Publishing to the drive_pwm topic
#   - The message type are drive_values
#   - The queue has a size '10' which describes the limited amount of queued messages
pub = rospy.Publisher('drive_pwm', drive_values, queue_size=10)

# pubBrake node is
#   - Publishing to the eStop topic
#   - The message type is Bool
#   - The queue has a size '10' which describes the limited amount of queued messages
pubBrake = rospy.Publisher('eStop', Bool, queue_size=10)


def callback(data):
    global input
    input = drive_values()
    input.pwm_angle = ((data.steer + 100) * 32.77) + 6554
    input.pwm_drive = ((data.throttle + 100) * 32.77) + 6554
    drive()

def brakeData(data):
    global brake
    brake = data.data
    drive()

def drive():
    global input, brake
    # If the car needs to brake publish backwards and turn wheel to show active braking
    if brake == "Brake":
        pubBrake.publish(true)
        print("Emergency braking")
        temp = drive_values()
        temp.pwm_angle =9831.0
        temp.pwm_drive =9700.0
        rospy.loginfo(input)
        pub.publish(temp)
    elif brake == "NoBrake":
        pubBrake.publish(false)
        pub.publish(input)

def listener():
    rospy.init_node('Talker', anonymous=True)
    rospy.Subscriber('drive_parameters', drive_param, callback)
    rospy.Subscriber('brake', String, brakeData)
    rospy.spin()


if __name__ == '__main__':
    listener()