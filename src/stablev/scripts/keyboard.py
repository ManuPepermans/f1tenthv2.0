#!/usr/bin/env python
import rospy
import curses
from std_msgs.msg import String
from race.msg import drive_param
stopped = None
steer = 0.0
throttle = 0.0

pub = rospy.Publisher('drive_parameters', drive_param, queue_size=10)

# get obstacle data, if there is an obstacle in front of the car reset values 
def callback(data):
    global stopped, steer, throttle

    if data == String('obs'):
        stopped = True
        steer = 0.0
        throttle = 0.0
    elif data == String('clear'):
          stopped = False
    
    msg = drive_param()
    msg.steer = steer
    msg.throttle = throttle 
    pub.publish(msg)

#read keyboard input, use arrows to increase or decrease speed or angle. Backspace to reset the values
def keyboardRace():
    global stopped, steer, throttle
    # Initializing the keyboard reader
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)
    
    rospy.init_node('keyboard', anonymous=True)
    rospy.Subscriber('obstruction', String, callback)
    stdscr.refresh()
    key = ''

    print("keyboard node started !")

    while not rospy.is_shutdown() and key != ord('q'):
        key = stdscr.getch()
        stdscr.refresh()
        if stopped == True:
            print("Obstacle")
        elif key == curses.KEY_UP:
            if throttle <= 100.0:
                throttle = throttle + 0.1
        elif key == curses.KEY_DOWN:
            if throttle >= -100.0:
                throttle = throttle - 0.1
        elif key == curses.KEY_LEFT:
            if steer > -100.0:
                steer = steer - 5
        elif key == curses.KEY_RIGHT:
            if steer < 100.0:
                steer = steer + 5
        elif key == curses.KEY_DC or key == curses.KEY_BACKSPACE:
            throttle = 0.0
            steer = 0.0

        msg = drive_param()
        msg.steer = steer
        msg.throttle = throttle
        print(msg)
        pub.publish(msg)

    curses.endwin()

if __name__ == '__main__':
    try:
        keyboardRace()
    except rospy.ROSInterruptException:
        pass
