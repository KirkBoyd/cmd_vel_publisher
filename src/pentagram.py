#! /usr/bin/env python

import rospy
import math
import time
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
vel = Twist()
vel.linear.x = 0
vel.linear.y = 0
vel.linear.z = 0
vel.angular.x = 0
vel.angular.y = 0
vel.angular.z = 0
count = 0


def callback(msg):
    global roll, pitch, yaw, ang, count, turn
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y,
                        orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
    ang = math.degrees(yaw)
    if ang < -1:
        ang = ang + 360
    if(ang <= 90):  # turn 0, also turn 5
        if(count < 2):
            count = 1
            vel.angular.z = 0.1
        if(count == 1 and ang >= 89):
            vel.angular.z = 0
            count = 2
    if(count == 2):    #
        vel.linear.x = 0.1
        time.sleep(20)
        vel.linear.x = 0
        count += 1
    if(count == 3):     # turn 1
        if(ang < 234):
            vel.angular.z = 0.1
        else:
            vel.angular.z = 0
            count = 4
    if(count == 4):
        vel.linear.x = 0.1
        time.sleep(20)
        vel.linear.x = 0
        count = 5
    if(count == 5):     # turn 2
        if(ang > 232 and ang < 361):
            vel.angular.z = 0.1
        elif(ang < 18):
            vel.angular.z = 0.1
        else:
            vel.angular.z = 0
            count = 6
    if (count == 6):
        vel.linear.x = 0.1
        time.sleep(20)
        vel.linear.x = 0
        count = 7
    if(count == 7):  # turn 3
        if(ang < 162):
            vel.angular.z = 0.1
        else:
            vel.angular.z = 0
            count = 8
    if (count == 8):
        vel.linear.x = 0.1
        time.sleep(20)
        vel.linear.x = 0
        count = 9
    if(count == 9):  # turn 4
        if(ang < 306):
            vel.angular.z = 0.1
        else:
            vel.angular.z = 0
            count = 10
    if(count == 10):
        vel.linear.x = 0.1
        time.sleep(20)
        vel.linear.x = 0
        count = 11
    if(count == 11):
        count = 1


rospy.init_node('pentagram')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/odom', Odometry, callback)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()
