'''
This function creates a file which stores the neural network output values of all the BGR values(256*256*256 values)
This file will be loaded at the start in a 3D array and then we will not apply the neural network on each pixel
but directly get its neural network output value from the 3D array.

The file is formatted as follows:
<value of 0,0,0>
<value of 0,0,1>
<value of 0,0,2>
.
.
<value of 0,0,255>
<value of 0,1,0>
<value of 0,1,1>
.
.
.
and so on 256*256*256 lines
'''
import network
import numpy as np
import pylab as pl

red = (1,0)
yellow = (0,1)
RED = 1
YELLOW = 2
NOT_A_BUOY = 0

def neuralNetwork(data):
	net1 = network.load("nnet")
	a = net1.feedforward(data)
	if a[0] >= 0.5 :
		a = (1,0)
	elif a[1] >= 0.5:
		a = (0,1)
	else :
		a = (0,0)
	return a

def storeBGR2Output():
	AllOutputs = open("AllOutputs.txt",'w');
	for i in range(256):
		for j in range(256):
			for k in range(256):
				val = neuralNetwork([i,j,k])	#Assumed that this function return the neural network output for BGR value i,j,k as 
											#(1,0) for red buoy, (0,1) for yellow buoy and (0,0) otherwise. Never returns (1,1)
				if val == red:
					val = RED
				elif val == yellow:
					val = YELLOW
				else:
					val = NOT_A_BUOY
				AllOutputs.write(str(val))
				AllOutputs.write("\n")

'''
This function load the file into the 3D array called NNOutput
'''
def loadNNOutputfile():
	AllOutputs = open("AllOutputs.txt",'r')
	NNOutput = [[[0 for i in range(256)] for j in range(256)] for k in range(256)]
	for i in range(256):
		for j in range(256):
			for k in range(256):
				NNOutput[i][j][k] = int(AllOutputs.readline())
	return NNOutput

# print neuralNetwork([74,105,87])
storeBGR2Output()