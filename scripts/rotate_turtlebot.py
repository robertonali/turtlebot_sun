#!/usr/bin/python

from logging import shutdown
from imutils.convenience import rotate
import rospy
from geometry_msgs.msg import Twist
from rospy.timer import Rate
from node_lf.msg import TbRot


def main():
    rospy.init_node('rotate_turtlebot')
    sub  = rospy.Subscriber('/topic_tb', TbRot, subCallback, queue_size=1)
    rospy.spin()
        
def subCallback(msg):
    pub  = rospy.Publisher('/cmd_vel',Twist, queue_size=1)
    rot = Twist()
    if msg.custom_msg=="1":
        rospy.loginfo(msg)
        rot.angular.z = 0.1
    elif msg.custom_msg=="2":
        rospy.loginfo(msg)
        rot.angular.z = 0.0
    elif msg.custom_msg=="3":
        rospy.loginfo(msg)
        rot.angular.z =-0.1
    else:
        rospy.loginfo(msg)
        rot.angular.z =-0.5
    pub.publish(rot)

if __name__ == "__main__":
    main()