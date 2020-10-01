#!/usr/bin/python

import cv2
import numpy as np
import imutils

    
cap = cv2.VideoCapture(0)

while True:
    
    _, frame = cap.read()
    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #red
    l_b = np.array([136, 115, 123])
    u_b = np.array([255, 255, 255])

    #light
    # l_b = np.array([0, 0, 255])
    # u_b = np.array([255, 68, 255])
    
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


    for i in cont:
        area   = cv2.contourArea(i)
        if area > 230:
            cv2.drawContours(res, i, -1, (0,255,0), 2)
            mns    = cv2.moments(i)
            cx     = int(mns["m10"]/mns["m00"])
            cy     = int(mns["m01"]/mns["m00"])
            cv2.circle(res,(cx,cy),7,(255,0,0),-1)
            cv2.imshow("contours", res)
            if 11 <= cx < 220:
                print(1)
            elif 220 <= cx < 429:
                print(2)
            elif 429<= cx < 638:
                print(3)
            else:
                pass


    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
 