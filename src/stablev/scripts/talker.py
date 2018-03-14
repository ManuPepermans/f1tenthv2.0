#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from race.msg import drive_param
from race.msg import drive_values

# initial values
input = drive_values()
input.pwm_angle = 9831.0
input.pwm_drive = 9831.0
obs = "clear"
brake = "NoBrake"

pub = rospy.Publisher('drive_pwm', drive_values, queue_size=10)


# read drive parameters and convert to values between 6554 and 13108
def inputData(data):
    global input
    input = drive_values()
    input.pwm_angle =((data.steer+100)*32.77)+6554 
    input.pwm_drive =((data.throttle+100)*32.77)+6554
    drive()        

# read obstacle data 
def ObstructionData(data):
    global obs
    obs = data.data
    drive()
 
# read brake data 
def brakeData(data):
    global brake
    brake = data.data
    drive()

# if the car needs to brake publish backwards and turn wheel to show active braking
# if there is an obstacle but no need to brake publish neutral 
# else publish drive paramters
def drive():
    global input, brake, obs
    if brake == "brake": 
       print("Emergency braking")
       temp = drive_values()
       temp.pwm_angle =11000.0 
       temp.pwm_drive =9700.0 
       print(temp)
       pub.publish(temp)
    elif brake == "NoBrake": 
        if obs == "clear":
            print("path is clear")
            print(input)
            pub.publish(input)
        else: 
            print("neutral") 
            temp = drive_values()
            temp.pwm_angle = 9831.0
            temp.pwm_drive = 9831.0
            pub.publish(temp)
        

def listener():
    print("Talker started")
    rospy.init_node('Talker',anonymous=True)
    rospy.Subscriber('brake',String, brakeData)
    rospy.Subscriber('obstruction', String, ObstructionData)
    rospy.Subscriber('drive_parameters', drive_param, inputData)
    drive()   
    rospy.spin()

if __name__ == '__main__':
    listener()
