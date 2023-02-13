#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move():
    # start a new node
    rospy.init_node('move_turtlesim', anonymous=True)
    # create a publisher to control the turtle's movement
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # set a constant linear velocity
    vel_msg.linear.x = 1.0

    # move the turtle
    while not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        if at_wall():
            vel_msg.linear.x = 0
            velocity_publisher.publish(vel_msg)
            rospy.loginfo("Turtle has reached the wall, stopping.")
            break

def at_wall():
    # check if the turtle has reached the wall
    pass # replace with appropriate code to check turtle's position

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass

