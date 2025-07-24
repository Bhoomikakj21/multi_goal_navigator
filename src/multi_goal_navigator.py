#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

pose = Pose()

waypoints = [(2, 2), (5, 5), (8, 2)]
current_goal_index = 0

def pose_callback(data):
    global pose
    pose = data

def move_to_waypoints():
    global current_goal_index
    rospy.init_node('multi_goal_navigator', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rate = rospy.Rate(10)
    vel_msg = Twist()

    while not rospy.is_shutdown():
        if current_goal_index >= len(waypoints):
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            rospy.loginfo("All goals reached.")
            break

        goal_x, goal_y = waypoints[current_goal_index]
        distance = math.sqrt((goal_x - pose.x)**2 + (goal_y - pose.y)**2)
        angle_to_goal = math.atan2(goal_y - pose.y, goal_x - pose.x)
        angle_error = angle_to_goal - pose.theta

        # Normalize angle error
        angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))

        vel_msg.linear.x = 1.5 * distance
        vel_msg.angular.z = 4.0 * angle_error

        if distance < 0.3:
            rospy.loginfo(f"Goal {current_goal_index + 1} reached.")
            current_goal_index += 1

        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_to_waypoints()
    except rospy.ROSInterruptException:
        pass
