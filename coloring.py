import cv2
import numpy as np

img = cv2.imread('img.jpg',0)
img1 = img;

def makeImg(color):
	for i in img.shape[0]:
		for j in img.shape[1]:
			if (color[img[i,j,0]][img[i,j,1]][img[i,j,2]] == 0):
				img1[i,j]=[255,255,255]
			else:
				if (color[img[i,j,0]][img[i,j,1]][img[i,j,2]] == 1):
					img1[i,j]=[0,0,255]
				else:
					if (color[img[i,j,0]][img[i,j,1]][img[i,j,2]] == 2):
						img1[i,j]=[0,255,255]
					else:
						print "error!!!"

	cv2.imshow('output',img1)

