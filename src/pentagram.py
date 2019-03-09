#! /usr/bin/env python

import rospy
import math
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
turn = False
deltaL = 0.1
deltaS = 0.01


def callback(msg):
    global roll, pitch, yaw, turn1
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y,
                        orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    if not turn1:
        turnTo(90)
    if turn1:
        goTo(x, y, 5)

    def turnTo(a):
        ang = math.degrees(yaw)
        if (ang < a-6):
            ang = math.degrees(yaw)
            vel.angular.z = 0.5
            turn1 = False
        elif (ang < a-deltaL):
            ang = math.degrees(yaw)
            vel.angular.z = 0.01
            turn1 = False
        elif (ang < a-deltaS):
            ang = math.degrees(yaw)
            vel.angular.z = 0.001
            turn1 = False
        elif (ang > a+deltaL):
            ang = math.degrees(yaw)
            vel.angular.z = -0.01
            turn1 = False
        elif (ang > a+deltaS):
            ang = math.degrees(yaw)
            vel.angular.z = -0.001
            turn1 = False
        else:
            vel.angular.z = 0
            turn1 = True

    def goTo(a, b, l):
        dist = math.sqrt(a*a + b*b)
        if (dist < l-1):
            dist = math.sqrt(a*a + b*b)
            vel.linear.x = 1
            print dist
        elif (dist < l-deltaL):
            dist = math.sqrt(a*a + b*b)
            vel.linear.x = 0.1
        elif (dist < l-deltaS):
            dist = math.sqrt(a*a + b*b)
            vel.linear.x = 0.01
            print dist
        elif (dist > l+deltaL):
            dist = math.sqrt(a*a + b*b)
            vel.linear.x = -0.1
        elif (dist > l+deltaS):
            dist = math.sqrt(a*a + b*b)
            vel.linear.x = -0.01
            print dist
        else:
            vel.linear.x = 0
            print "done"


rospy.init_node('pentagram')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/odom', Odometry, callback)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()
