#!/usr/bin/env python3
import rospy

#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('input_user')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
move = Twist()

move.linear.x  = float(input("Enter linear velocity in the range [2,6]: "))
while move.linear.x < 2 or move.linear.x > 6:
	move.linear.x = float(input("Invalid input. Enter a linear velocity between 2 and 6: "))

move.angular.z = float(input("Enter angular velocity in the range [1,3]: "))
while move.angular.z < 1 or move.angular.z > 3:
        move.angular.z = float(input("Invalid input. Enter an angular velocity between 1 and 3: "))


while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()
    
if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass

