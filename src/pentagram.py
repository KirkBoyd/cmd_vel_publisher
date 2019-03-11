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
global turn1, turn2, turn3, turn4, turn5
# turn1 = False
# turn2 = False
# turn3 = False
# turn4 = False
# turn5 = False
count = 0
delta = 2


def callback(msg):
    global roll, pitch, yaw, ang, pos, count, turn

    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y,
                        orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    pos = math.sqrt(x*x + y*y)
    ang = math.degrees(yaw)
    if ang < -1:
        ang = ang + 360
    if(ang <= 90):  # turn 0, also turn 5
        if(count < 2):
            print ang
            count = 1
            print "count = 1"
            vel.angular.z = 0.1
        if(count == 1 and ang >= 89):
            vel.angular.z = 0
            count = 2
            print "count = 2"

    if(count == 2):
        vel.linear.x = 0.1
        print "going to sleep"
        time.sleep(20)
        vel.linear.x = 0
        count = 3
        print "count = 3"

    if(count == 3):     # turn 1
        if(ang < 234):
            print ang
            vel.angular.z = 0.1
        else:
            vel.angular.z = 0
            count = 4
            print "count = 4"

    if(count == 4):
        vel.linear.x = 0.1
        print "going to sleep 2nd time"
        time.sleep(20)
        vel.linear.x = 0
        count = 5
        print "count = 5"

    if(count == 5):     # turn 2
        if(ang > 232 and ang < 361):
            print ang
            vel.angular.z = 0.1
        elif(ang < 18):
            print ang
            vel.angular.z = 0.1
        else:
            vel.angular.z = 0
            count = 6
            print "count = 6"

    if (count == 6):
        vel.linear.x = 0.1
        print "going to sleep 3rd time"
        time.sleep(20)
        vel.linear.x = 0
        count = 7
        print "count = 7"

    if(count == 7):  # turn 3
        if(ang < 162):
            print ang
            vel.angular.z = 0.1
        else:
            vel.angular.z = 0
            count = 8
            print "count = 8"

    if (count == 8):
        vel.linear.x = 0.1
        print "going to sleep 4th time"
        time.sleep(20)
        vel.linear.x = 0
        count = 9
        print "count = 9"

    if(count == 9):  # turn 4
        if(ang < 306):
            print ang
            vel.angular.z = 0.1
        else:
            vel.angular.z = 0
            count = 10
            print "count = 10"

    if(count == 10):
        vel.linear.x = 0.1
        print "going to sleep 5th time"
        time.sleep(20)
        vel.linear.x = 0
        count = 11
        print "count = 11"

    if(count == 11):
        count = 1
        print "count = 1"


rospy.init_node('pentagram')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/odom', Odometry, callback)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()
