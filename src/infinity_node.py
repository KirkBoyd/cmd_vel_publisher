#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 
PI = 3.1415926535897

rospy.init_node('infinity_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
vel = Twist()
vel.linear.x = 0
vel.linear.y = 0
vel.linear.z = 0
vel.angular.x = 0
vel.angular.y = 0
vel.angular.z = 0

r = 2
circ = 2*PI*r
dist = 0

while not rospy.is_shutdown():
    t0 = rospy.TimeNow().to_sec()
    while dist < circ:
        pub.publish(vel)
        t1 = rospy.Time.now().to_sec()
        dist = vel.linear.x*(t1-t0)
        vel.linear.x = 1
        vel.angular.z = 0.5
        
    while dist>circ:
        pub.publish(vel)
        t1 = rospy.Time.now().to_sec()
        dist = vel.linear.x*(t1-t0)
        vel.linear.x = 1
        vel.angular.z = 0.5
    
    if dist==2*circ:
        dist = 0;
  
  rate.sleep()