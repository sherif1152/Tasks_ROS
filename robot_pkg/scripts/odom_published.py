#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def publish_odometry():
    rospy.init_node('odom_published')
    pub = rospy.Publisher('odometry', Odometry, queue_size=10)
    rate = rospy.Rate(10)  
    odom = Odometry()

    while not rospy.is_shutdown():
        odom.header.stamp = rospy.Time.now()
        odom.pose.pose.position.x = 0
        odom.pose.pose.position.y = 0
        odom.pose.pose.position.z = 0
        odom.pose.pose.orientation.x = 0
        odom.pose.pose.orientation.y = 0
        odom.pose.pose.orientation.z = 0
        odom.pose.pose.orientation.w = 1

        pub.publish(odom)

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_odometry()
    except rospy.ROSInterruptException:
        pass

