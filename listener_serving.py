#!/usr/bin/env python


import rospy
from msg_server.msg import custom

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+ 'Data: %s', data.c)

def listener():

    
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('coffee', custom, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
