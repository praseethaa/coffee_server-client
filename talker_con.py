#!/usr/bin/env python


import rospy
from msg_server.msg import custom

def talker():
    pub = rospy.Publisher('coffee', custom, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    N=custom()
    while not rospy.is_shutdown():
        N.a="Sugar,Milk"
        N.b="Mixing proportion"
        N.c= "Serve on table"
        rospy.loginfo(N)
        pub.publish(N)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
