import data_loader
import network
import numpy as np
import pylab as pl


"""If we want to train our neural network"""
## training data is like a list where each element of the list is a data set and its answer in matrix form
training_data, validation_data, test_data = data_loader.load_data()
for i in range(0,len(validation_data)):
	validation_data[i][1] = np.argmax(validation_data[i][1])
for i in range(0,len(test_data)):
	test_data[i][1] = np.argmax(test_data[i][1])

O = 3
I = 3
S = len(training_data)
H = int((S/3-O)/(I+O+1))

net = network.Network([I, H ,O] ,cost=network.CrossEntropyCost, plot = True)
net.SGD(training_data,30,10,0.1,lmbda=5.0,evaluation_data = validation_data ,monitor_evaluation_accuracy=True,monitor_training_accuracy=True)

"""If we want to test on any dataset"""

# f = open("array.txt")
# data = f.read()
# f.close()
# data = data.split("\n")
# a = []
# for d in data:
# 	split_row = map(float,d.split(" "))
# 	for s in split_row:
# 		a.append([s])
# a = np.asarray(a)
# net1 = network2.load("nnet_97.83")
# print "Predicted Answer:",np.argmax(net1.feedforward(a))

# net1 = network.load("nnet")
# print float(net1.accuracy(validation_data))/len(validation_data) * 100


# red_buoy_data = open("Data/filtered_water_data.txt",'r')
# Rdata = []
# red_buoy = np.array([0,0,1])
# lines = red_buoy_data.readlines()
# for line in lines:
#     Rdata.append( [[float(x)/256 for x in line.split()],red_buoy] )

# for i in range(0,len(Rdata)):
# 	Rdata[i][1] = np.argmax(Rdata[i][1])
# net1 = network.load("nnet")
# print float(net1.accuracy(Rdata))/len(Rdata) * 100
