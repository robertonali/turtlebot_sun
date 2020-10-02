#!/usr/bin/env python
# license removed for brevity

import rospy
from node_lf.msg import TbRot
    
rospy.init_node('topic_publisher', anonymous=True)
pub = rospy.Publisher('/topic_tb', TbRot, queue_size=10)
rate = rospy.Rate(1) # 10hz
message = TbRot()
message.custom_msg = "hello world %s" % rospy.get_time()

while not rospy.is_shutdown():
    pub.publish(message)
    rate.sleep()

