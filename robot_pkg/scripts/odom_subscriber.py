#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def listener():
    rospy.init_node('listener',anonymous=True )
    rospy.Subscriber("odometry", Odometry, callback)
    rospy.spin()

def callback(data):
    rospy.loginfo("Received odometry data:")
    rospy.loginfo("\tPosition: x=%f, y=%f, z=%f", data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z)
    rospy.loginfo("\tOrientation: x=%f, y=%f, z=%f, w=%f", data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w)


if __name__ == '__main__':
    listener()

