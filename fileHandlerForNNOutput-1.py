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
import time

red = (1,0,0)
yellow = (0,1,0)
RED = 0
YELLOW = 1
NOT_A_BUOY = 2

def neuralNetwork(data):
	net1 = network.load("nnet")
	a = net1.feedforward(data)
	a = a/sum(a)
	a = np.around(a, decimals=3)
	# print "Probabilities : ",a
	if a[0] > 0.5 :
		a = (1,0,0)  #Red
	elif a[1] > 0.5:
		a = (0,1,0)  #yellow
	else :
		a = (0,0,1)  #water
	return a

def storeBGR2Output():
        start_time = time.time()
        step_2_times = []
	AllOutputs = open("AllOutputs.txt",'w');
	for i in range(256):
                print "Running loop level 1: %d of 256" % i
		for j in range(256):
                        start_time = time.time()
                        print "  Running loop level 2: %d of 256 at %0.2f." % (j, time.time())
			for k in range(256):
				val = neuralNetwork([i/256.0,j/256.0,k/256.0])	# pass BGR value to the NN

                                # print "    Running loop level 3: %d of 256" % k
				# val = neuralNetwork([i,j,k])	#Assumed that this function return the neural network output for BGR value i,j,k as 
											#(1,0) for red buoy, (0,1) for yellow buoy and (0,0) otherwise. Never returns (1,1)
				if val == red:
					val = RED
				elif val == yellow:
					val = YELLOW
				else:
					val = NOT_A_BUOY
				AllOutputs.write(str(val))
				AllOutputs.write("\n")

                        end_time = time.time()
                        total_step_2_time = end_time - start_time
                        step_2_times.append(total_step_2_time)
                        # print step_2_times
                        print "  -- Average time for level 2 array: %0.2f" % (sum(step_2_times) / len(step_2_times))


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

# val = neuralNetwork(data)
# if val == red:
# 	val = RED
# elif val == yellow:
# 	val = YELLOW
# else:
# 	val = NOT_A_BUOY
# print val
storeBGR2Output()
# print neuralNetwork([74,105,87])
