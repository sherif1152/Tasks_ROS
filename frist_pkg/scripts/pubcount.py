#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def count_publisher():
    # Initialize the node
    rospy.init_node('count_publisher', anonymous=True)
    # Create a publisher
    pub = rospy.Publisher('count_topic', Int32, queue_size=10)
    # Set the rate at which messages will be published
    rate = rospy.Rate(1)
    # Get the number to count up to from the user
    count_to = int(input("Enter a number to count up to: "))
    # Start counting
    count = 0
    while not rospy.is_shutdown():
        # Publish the current count
        pub.publish(count)
        # Sleep for the rate
        rate.sleep()
        # Increment the count
        count += 1
        # Exit the loop if the count has reached the number entered by the user
        if count > count_to:
            break

if __name__ == '__main__':
    try:
        count_publisher()
    except rospy.ROSInterruptException:
        pass
