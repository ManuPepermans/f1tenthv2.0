#!/usr/bin/env python


import rospy
import curses
from std_msgs.msg import String

pub = rospy.Publisher('emergency', String, queue_size=10)

# reads keyboard input, backspace to brake manually
def emergency():
 
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)

 
    rospy.init_node('emergencyNode', anonymous=True)
    stdscr.refresh()
    key = ''

 
    print("emergency node started !")
    print("push backspace to brake !")


    while not rospy.is_shutdown() and key != ord('q'):
        key = stdscr.getch()
        stdscr.refresh()
        if key == curses.KEY_BACKSPACE:
            pub.publish('obs')
            print("emergency brake !")
	elif key == ord('\\'):
	    pub.publish('clear')        


    curses.endwin()

if __name__ == '__main__':
    try:
        emergency()
    except rospy.ROSInterruptException:
        pass
