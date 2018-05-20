#!/usr/bin/env python
#
# Copyright (c) 2018, University of Antwerp.
# All rights reserved.
#
# Jens de Hoog, Stevie Maes, Bernd Smits, Jonas Vercauteren

import rospy
import curses
# std_msgsmsg uses the message type String for publishing
from std_msgs.msg import String

# pub node is
#   - Publishing to the emergency topic
#   - The message type is String
#   - The queue has a size '10' which describes the limited amount of queued messages
pub = rospy.Publisher('emergency', String, queue_size=10)

# Reads keyboard input, backspace to brake manually
def emergency():

    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)

    rospy.init_node('navEmergencyNode', anonymous=True)
    stdscr.refresh()
    key = ''

    print("Navigation emergency node enabled:")
    print("Backspace to brake!")

    # While rospy is not down and 'q' is not pressed to quit
    while not rospy.is_shutdown() and key != ord('q'):

        key = stdscr.getch()
        stdscr.refresh()

        if key == curses.KEY_BACKSPACE:
            pub.publish('Brake')
            print("emergency brake !")
        elif key == ord('\\'):
            pub.publish('Deny')

    curses.endwin()

if __name__ == '__main__':
    try:
        emergency()
    except rospy.ROSInterruptException:
        pass
