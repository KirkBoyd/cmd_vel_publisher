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
turn = False
count = 1
x = 0
y = 0

def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

def originCheck():
    if x==0 & y==0:
        count *= -1
    else
        count = 1
        
            
rospy.init_node('infinity_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/odom', Odometry, callback)
rate = rospy.Rate(2)


while not rospy.is_shutdown():

    while count == -1:
        vel.angular.z = -0.5
        pub.publish(vel)
        originCheck

    while count == 1:
        vel.angular.z = 0.5
        pub.publish(vel)
        originCheck
  
    rate.sleep()