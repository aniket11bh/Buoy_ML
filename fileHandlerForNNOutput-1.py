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
import sys
import os
import shutil

red = (1,0,0)
yellow = (0,1,0)
RED = 0
YELLOW = 1
NOT_A_BUOY = 2


def neuralNetwork(data):
	"""
	Calculates the output of NN for particular normalized BGR / YUV values
	VAlues can be changed : Threshold for Red, yellow and water

	Input : list of normalized BGR or YUV values

	output : 
	"""
	net1 = network.load("nnet")
	a = net1.feedforward(data)
	a = a/sum(a)
	a = np.around(a, decimals=3)
	# print "Probabilities : ",a
	if a[0] > 0.72 :
		a = (1,0,0)  #Red
	elif a[1] > 0.72:
		a = (0,1,0)  #yellow
	else :
		a = (0,0,1)  #water
	return a

def storeBGR2Output(start_index, end_index):
	"""
	Stores output of NN for a range of BGR / YUV values into a text file named by it's range

	Input : 
		- start_index : Starting vlaue of B or  Y
		- end_index   : End value of B or Y

	"""
        start_time = time.time()
        step_2_times = []
        main_file_name = 'main_' + str(start_index) + "-" + str(end_index) + ".txt"
	AllOutputs = open(main_file_name, 'w');
        op_start_time = time.time()
	for i in range(start_index, end_index):
                print "Running loop level 1: %d of 256" % i
		for j in range(256):
                        start_time = time.time()
                        print "  %d of 256 and %d of 256" % (i, j)
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

                        # print "Stats print start at %0.2f" % time.time()

                        end_time = time.time()
                        total_step_2_time = end_time - start_time
                        step_2_times.append(total_step_2_time)

                        average_time = (sum(step_2_times) / len(step_2_times))
                        percentage_done = (j + 1 + (i-start_index) * 256) / (float(end_index-start_index) * 256) * 100
                        time_remaining = ((end_time - op_start_time) / percentage_done * 100 / 60) if percentage_done != 0 else 3600

                        print "  -- Average time for level 2 array: %0.2f" % average_time
                        print "  -- Percentage of total work done : %0.6f percent" % percentage_done
                        print "  -- Remaining time                : %0.3f minutes" % time_remaining

                        # print "Stats print stop at %0.2f" % time.time()

                        # backup_file_name = 'backup_' + str(start_index) + '-' + str(i+1) + '.txt'

                        # os.system('cp ' + main_file_name + ' ' + backup_file_name)

        AllOutputs.close()


def loadNNOutputfile():
	"""
	This function load the file into the 3D array called NNOutput

	Input : NONE

	output : 3D array

	"""
	
	AllOutputs = open("AllOutputs.txt",'r')
	NNOutput = [[[0 for i in range(256)] for j in range(256)] for k in range(256)]
	for i in range(256):
		for j in range(256):
			for k in range(256):
				NNOutput[i][j][k] = int(AllOutputs.readline())
	return NNOutput

##### For checking the output of NN

# data = ([224, 218, 87])
# for i in range(len(data)) :
# 	data[i] = float(data[i])/256
# val = neuralNetwork(data)
# if val == red:
# 	val = RED
# elif val == yellow:
# 	val = YELLOW
# else:
# 	val = NOT_A_BUOY
# print val


##### For generation of 3D array

if len(sys.argv) == 3:
    start_glob = int(sys.argv[1])
    end_glob = int(sys.argv[2])
else:
    if len(sys.argv) == 2:
        start_glob = int(sys.argv[1])
        end_glob = start_glob + 1
    else:
        print "You need to provide atleast the start index"
        sys.exit(0)
storeBGR2Output(start_glob, end_glob)
