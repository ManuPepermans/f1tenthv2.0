#!/usr/bin/env python

import rospy
from race.msg import drive_param
from race.msg import pid_input
from std_msgs.msg import String
from std_msgs.msg import Float32

# Make a publisher on the topic "drive_parameters"
pub = rospy.Publisher('drive_parameters', drive_param, queue_size=1)

# Define Global Values
kp = 14.0 * 4.5
ki = 20.0
kd = 0.09 * 4.5
vel_input = 0.0
prev_error = 0.0
angle = 0.0
prev_angle = 0.0
angleTemp = 9000.0
reset = False
speedDivider = 4.0

# On a brake from distFinder we stop the car
def stop(data):
    global reset
    if (data.data == 'brake'):
        reset = True
        print("Reset: ",reset)

# An angle from cornerFinder or turnAround is read into angleTemp
def cornerAdjust(data):
   global angleTemp, speed
   angleTemp = data.data
   print(data)

# Controls the values sent to the talker
def control(data):
    global kp, kd, servo_offset, prev_error
    global vel_input, angle, prev_angle, curr_time, prev_time
    vel_input = data.pid_vel
    if reset is True: # Stop the car
        vel_input = 0.0
        angle = 0.0
    elif reset is False: # Continue the normal operation
        if angleTemp != 9000 and angleTemp != 10000:
            if angleTemp == 9500: # Drive backwards left
                msg = drive_param()
                msg.throttle = -(vel_input/speedDivider)
                msg.steer = -100
                pub.publish(msg)
            elif angleTemp == 9600: # Drive backwards right
                msg = drive_param()
                msg.throttle = -(vel_input/speedDivider)
                msg.steer = 100
                pub.publish(msg)
            elif angleTemp == 9700: # Drive forward right
                msg = drive_param()
                msg.throttle = vel_input/speedDivider
                msg.steer = 100
                pub.publish(msg)
            elif angleTemp == 9800: # Drive forward left
                msg = drive_param()
                msg.throttle = vel_input/speedDivider
                msg.steer = -100
                pub.publish(msg)
            elif angleTemp == 9900: # Put car in neutral
                msg = drive_param()
                msg.throttle = 0.0
                msg.steer = 0.0
                pub.publish(msg)
            else:
                msg = drive_param()
                msg.throttle = vel_input/2
                msg.steer = angleTemp
                pub.publish(msg)
        elif angleTemp == 9000 or angleTemp == 10000:
            pid_error = data.pid_error
            # Proportional
            error = kp * pid_error
            # Integral
            curr_time = rospy.Time.now().secs
            deltaT = curr_time - prev_time
            errordot = ki * (deltaT * pid_error)
            # Derivative
            errordotdot = kd * (pid_error - prev_error)

            angle = error + errordot + errordotdot

            if angle > 100:
                angle = 100
            elif angle < -100:
                angle = -100

            prev_error = pid_error
            prev_time = curr_time

            #print 'pid_error {}\nangle {}'.format(pid_error, angle)

            # Publish speed and angle only when values change
            thresh = 0.0
            if abs(angle) > abs(prev_angle) + thresh or abs(angle) < abs(prev_angle) - thresh:
                msg = drive_param()
                if angleTemp == 10000:
                    msg.throttle = vel_input/speedDivider
                else:
                    msg.throttle = vel_input
                msg.steer = angle
                pub.publish(msg)
                prev_angle = angle

if __name__ == '__main__':
    print("Listening to error for PID")
    rospy.init_node('MiddleofRoadControl', anonymous=True)
    curr_time = rospy.Time.now().secs
    prev_time = curr_time
    rospy.Subscriber('error', pid_input, control)
    rospy.Subscriber('brake', String, stop)
    rospy.Subscriber('cornerOrWall', Float32, cornerAdjust)
    rospy.spin()
