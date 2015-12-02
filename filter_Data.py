import numpy as np
import statistics
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def filter_data(data):
    dataR = []
    dataG = []
    dataB = []
    for datapoint in data:
        dataR.append(datapoint[2])
        dataG.append(datapoint[1])
        dataB.append(datapoint[0])
    avgR = statistics.mean(dataR)
    stdDevR = statistics.pstdev(dataR,avgR)
    avgG = statistics.mean(dataG)
    stdDevG = statistics.pstdev(dataG,avgG)
    avgB = statistics.mean(dataB)
    stdDevB = statistics.pstdev(dataB,avgB)

    # Based on assumption that 95% of data is approximately in the range of twice the std deviation from mean
    # If we want only 68% data we may use a range of within 1 std deviation

    filteredData = []
    for datapoint in data:
        if datapoint[2]<avgR+2*stdDevR and datapoint[2]>avgR-2*stdDevR and datapoint[1]<avgG+2*stdDevG and datapoint[1]>avgG-2*stdDevG and datapoint[0]<avgB+2*stdDevB and datapoint[0]>avgB-2*stdDevB:
            filteredData.append(datapoint)

    return filteredData

def remove_redundant(data):
    colour_present = [[[0 for col in range(256)]for row in range(256)] for x in range(256)]
    for datapoint in data:
        colour_present[datapoint[0]][datapoint[1]][datapoint[2]] = 1
    del data[:]
    for i in range(256):
        for j in range(256):
            for k in range(256):
                if(colour_present[i][j][k] == 1):
                    data.append([i,j,k])
    return data

def plot_data(data):
    """Scatter plot of the datapoints"""

    data_x = []
    data_y = []
    data_z = []
    c      = []

    for datapoint in data:
        data_x.append(datapoint[2])
        data_y.append(datapoint[1])
        data_z.append(datapoint[0])
        c.append([datapoint[2]/256.0,datapoint[1]/256.0,datapoint[0]/256.0])
        # Since BGR instead of RGB => R = X, G = Y, B = Z

    scatter_red_buoy = ax.scatter(data_x, data_y, data_z, c = c)

    c_demo = [[1,0,0],[0,1,0],[0,0,1]]
    RGB = [[255,0,0],[0,255,0],[0,0,255]]
    scatter_demo = ax.scatter(RGB[0],RGB[1],RGB[2], c = c_demo)

    # print [[datapoint[0]/256.0,datapoint[1]/256.0,datapoint[2]/256.0]]
    ax.set_zlim3d(0, 255) 
    ax.set_xlim3d(0, 255) 
    ax.set_ylim3d(0, 255) 
    ax.set_xlabel('RED', fontsize = 10)
    ax.set_ylabel('GREEN', fontsize = 10)
    ax.set_zlabel('BLUE', fontsize = 10)



fig = plt.figure()
ax = Axes3D(plt.gcf())   # ax = plt.subplot(111, projection='3d')
datafile = open("/home/aniket/Desktop/Priyank/train_file_yellow.txt",'r')
data = []
lines = datafile.readlines()
for line in lines:
    data.append([int(x) for x in line.split()])
datafile.close()
data = remove_redundant(data)
data1 = filter_data(data)

# datafile = open("/home/aniket/Desktop/Priyank/train_file_yellow.txt",'r')
# data = []
# lines = datafile.readlines()
# for line in lines:
#     data.append([int(x) for x in line.split()])
# datafile.close()
# data = remove_redundant(data)
# data2 = filter_data(data)


plot_data(data1)
# plot_data(data2)
plt.show()





# filtered_data_file = open("filtered_train_data_yellow.txt",'w')
# for datapoint in data:
#     filtered_data_file.write(str(datapoint[0]) + " " + str(datapoint[1]) + " " + str(datapoint[2]) + "\n")
# datafile.close()
# filtered_data_file.close()
