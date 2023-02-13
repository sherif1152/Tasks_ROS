#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def count_callback(data):
    # Print the received count
    print("Count: ", data.data)

def count_subscriber():
    # Initialize the node
    rospy.init_node('count_subscriber', anonymous=True)
    # Create a subscriber
    rospy.Subscriber("count_topic", Int32, count_callback)
    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    count_subscriber()
