#!/usr/bin/env python

import rospy
# std_msgs.msg uses the message type String for publishing
from std_msgs.msg import String
#from std_msgs.msg import Bool
# race.msg uses the messages type drive_param, drive_values for publishing
from race.msg import drive_param
from race.msg import drive_values

# initial values
input = drive_values()
input.pwm_angle = 9831.0
input.pwm_drive = 9831.0
obs = "clear"
brake = "NoBrake"

# This node is
#   - Publishing to the drive_pwm topic
#   - The message type is drive_values
#   - The queue has a size '10' which describes the limited amount of queued messages
pub = rospy.Publisher('drive_pwm', drive_values, queue_size=10)
#pubBrake = rospy.Publisher('eStop', Bool, queue_size=10)


# Read drive parameters and convert to values between 6554 and 13108
def inputData(data):
    global input
    input = drive_values()
    input.pwm_angle =((data.steer+100)*32.77)+6554 
    input.pwm_drive =((data.throttle+100)*32.77)+6554
    drive()        

# Read obstacle data
def ObstructionData(data):
    global obs
    obs = data.data
    drive()
 
# Read brake data
def brakeData(data):
    global brake
    brake = data.data
    drive()

def drive():
    global input, brake, obs
    # If the car needs to brake publish backwards and turn wheel to show active braking
    if brake == "brake":
       #pubBrake.publish(true)
       print("Emergency braking")
       temp = drive_values()
       temp.pwm_angle =11000.0
       temp.pwm_drive =9700.0
       print(temp)
       pub.publish(temp)
    elif brake == "NoBrake":
        #pubBrake.publish(false)
        # If there is no obstacle, just publish drive paramters
        if obs == "clear":
            print("path is clear")
            print(input)
            pub.publish(input)
        # If there is an obstacle but no need to brake publish neutral, car will put himself into neutral
        else: 
            print("neutral") 
            temp = drive_values()
            temp.pwm_angle = 9831.0
            temp.pwm_drive = 9831.0
            pub.publish(temp)
        

def listener():
    print("Talker started")
    # It tells rospy the name of the node which is Talker, anonymous=true
    rospy.init_node('Talker',anonymous=True)
    # Subscribing to emergency to receive String data which will trigger the brakeData function
    rospy.Subscriber('brake',String, brakeData)
    # Subscribing to emergency to receive String data which will trigger the ObstructionData function
    rospy.Subscriber('obstruction', String, ObstructionData)
    # Subscribing to emergency to receive drive_param data which will trigger the inputData function
    rospy.Subscriber('drive_parameters', drive_param, inputData)
    drive()   
    rospy.spin()

if __name__ == '__main__':
    listener()
