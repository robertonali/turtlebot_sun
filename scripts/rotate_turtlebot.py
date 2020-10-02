#!/usr/bin/python

from logging import shutdown

from imutils.convenience import rotate
import rospy
from geometry_msgs.msg import Twist
from rospy.timer import Rate
from node_lf.msg import TbRot
from std_msgs.msg import String


def main():
    rospy.init_node('rotate_turtlebot')
    #pub  = rospy.Publisher('/cmd_vel',Twist, queue_size=1)
    sub  = rospy.Subscriber('/topic_tb', TbRot, subCallback, queue_size=1)
    rospy.spin()
# class rotate_bot(object):
#     def __init__(self,pub):
#         self.pub=pub
        
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

# def main():
#     rospy.init_node('rotate_turtlebot')
#     pub  = rospy.Publisher('/cmd_vel',Twist, queue_size=1)
#     robot= rotate_bot(pub)
#     sub  = rospy.Subscriber('/topic_tb', TbRot, rotate_bot.subCallback, queue_size=1)
#     rospy.spin()
if __name__ == "__main__":
    main()