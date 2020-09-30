#!/usr/bin/python

from logging import shutdown
import rospy
from geometry_msgs.msg import Twist
from rospy.timer import Rate

rospy.init_node('rotate_turtlebot')

pub=rospy.Publisher('/cmd_vel',Twist, queue_size=1)
rate=rospy.Rate(1)
rot=Twist()
var=2
if var==1:
    rot.angular.z =0.1
elif var==2:
    rot.angular.z =0.0
elif var==3:
    rot.angular.z =-0.1
else:
    rot.angular.z =-0.5

while not rospy is shutdown:
    pub.publish(rot)
    rate.sleep()