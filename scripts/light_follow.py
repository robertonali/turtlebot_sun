#!/usr/bin/python

import cv2
import numpy as np
import imutils

def nothing(x):
    pass
cap = cv2.VideoCapture(0);

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    # l_b = np.array([133, 161, 71])
    # u_b = np.array([255, 255, 255])
    
    mask = cv2.inRange(hsv, l_b, u_b)

    # lower_red = np.array([0,50,50])
    # upper_red = np.array([10,255,255])
    # mask0 = cv2.inRange(frame, lower_red, upper_red)

    # # upper mask (170-180)
    # lower_red = np.array([170,50,50])
    # upper_red = np.array([180,255,255])
    # mask1 = cv2.inRange(frame, lower_red, upper_red)

    # # join my masks
    # mask = mask0+mask1
    res  = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    cont = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont = imutils.grab_contours(cont)

    cont_list  = []
    max1       = 0
    maxcont    = 0

    # for i in cont:
    #     area   = cv2.contourArea(i)
    #     if area > 110:
    #         if area > max1:
    #             max1 = area
    #             maxcont=i
    
    # cv2.drawContours(frame, maxcont, -1, (0,255,0), 2)
    # mns    = cv2.moments(maxcont)
    # cx     = int(mns["m10"]/mns["m00"])
    # cy     = int(mns["m01"]/mns["m00"])
    # cv2.circle(frame,(cx,cy),7,(255,0,0),-1)
    # cv2.imshow("contours", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()