#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import cv2
import numpy as np
import imutils
from node_lf.msg import TbRot

def publ():
    pub = rospy.Publisher('/topic_tb', TbRot, queue_size=1)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    case = TbRot()
    while not rospy.is_shutdown():
        cap=cv2.VideoCapture(0)
        while True:
            _ , frame = cap.read()

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            l_b = np.array([133, 161, 71])
            u_b = np.array([255, 255, 255])

            mask= cv2.inRange(hsv, l_b, u_b)
            res = cv2.bitwise_and(frame,frame, mask=mask)

            cv2.imshow("frame", frame)
            cv2.imshow("mask", mask)
            cv2.imshow("res", res)
            cont = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cont = imutils.grab_contours(cont)

            for i in cont:
                area = cv2.contourArea(i)
                if area > 230:
                    cv2.drawContours(res, i, -1, (0,255,0),2)
                    mns = cv2.moments(i)
                    cx  = int(mns["m10"]/mns["m00"])
                    cy  = int(mns["m01"]/mns["m00"])
                    cv2.circle(res,(cx,cy),7,(255,0,0),-1)
                    cv2.imshow("contours", res)
                    if 11<= cx < 220:
                        case.custom_msg = "1"
                        pub.publish(case)
                        # rate.sleep()
                    elif 220 <= cx < 429:
                        case.custom_msg = "2"
                        pub.publish(case)
                        # rate.sleep()
                    elif 429 <= cx < 638:
                        case.custom_msg = "3"
                        pub.publish(case)
                        # rate.sleep()
                    else:
                        pass
            key = cv2.waitKey(1)
            if key == 27:
                break
        # rospy.loginfo(case)
        # cap.release()
        # cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        publ()
    except rospy.ROSInterruptException:
        pass