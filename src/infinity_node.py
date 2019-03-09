#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
vel = Twist()
vel.linear.x = 0.5
vel.linear.y = 0
vel.linear.z = 0
vel.angular.x = 0
vel.angular.y = 0
vel.angular.z = -0.25
turn = False


def callback(msg):
    global turn
    x = msg.pose.pose.position.x
    print("x")
    print(x)
    y = msg.pose.pose.position.y
    print("y")
    print(y)
    if (-0.02 < x and x < 0.015) and (-0.01 < y and y < 0.003):
        turn = not turn
        if turn:
            vel.angular.z = 0.25
            vel.linear.x = 0.5
        else:
            vel.angular.z = -0.25
            vel.linear.x = 0.5


rospy.init_node('infinity_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/odom', Odometry, callback)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()
