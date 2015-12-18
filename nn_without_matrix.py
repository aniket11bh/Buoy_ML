import cv2
import time
import numpy as np
from fileHandlerForNNOutput1 import neuralNetwork 

img = cv2.imread('./sample_images/2.png',cv2.IMREAD_COLOR)
img1 = img;

def makeImg():
	avoid = [[[-1 for i in range(256)] for j in range(256)] for k in range(256)]
        print "image dimensions: %d %d" % (img.shape[0], img.shape[1])
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if avoid[img[i,j,0]][img[i,j,1]][img[i,j,2]] == -1:
			    a = neuralNetwork([img[i,j,0]/256.0,img[i,j,1]/256.0,img[i,j,2]/256.0])
			    avoid[img[i,j,0]][img[i,j,1]][img[i,j,2]] = a
			else:
				a = avoid[img[i,j,0]][img[i,j,1]][img[i,j,2]]
			if a[0] == 1:
				img1[i,j]=[0,0,0]
			else:
				if a[1] == 1:
					img1[i,j]=[0,0,255]
				else:
					if a[2] == 1:
						img1[i,j]=[0,255,255]
					else:
                                                raise RuntimeError("Value of a must be 0 1 or 2, but it was " + str(a))
			# if(a!=0):
			# 	print str(i) + " , " + str(j) + " : " + str(a)

	# cv2.imshow('output',img1)
        filename = 'output-images/output-' + str(int(time.time())) + '.png'
        cv2.imwrite(filename, img1)
        print "Written to %s" % filename
	# cv2.waitKey(3000)

makeImg()
