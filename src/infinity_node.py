#! /usr/bin/env python

import rospy
#from time import sleep
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry
vel = Twist()
vel.linear.x = 1
vel.linear.y = 0
vel.linear.z = 0
vel.angular.x = 0
vel.angular.y = 0
vel.angular.z = 0
global turn 

def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    if x==0.0 & y==0.0:
        turn != turn
    if turn:
        vel.angular.z = 0.5
    else:
        vel.angular.z = -0.5     
            
rospy.init_node('infinity_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/odom', Odometry, callback)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()