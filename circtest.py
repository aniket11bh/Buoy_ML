import cv2
import cv2.cv as cv
import numpy as np

img = cv2.imread('/home/barno/Pictures/Screenshot from 2015-12-15 19:46:53.png',0)
cv2.imshow('src',img)
# img = cv2.medianBlur(img,25)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cimg = img
circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=15,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    print i[0]
    print i[1]

cv2.imshow('detected circles',img)

cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()

