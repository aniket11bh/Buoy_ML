"""
data_loader
~~~~~~~~~~~~

data_loader is the function usually called by our neural network
code to load the data of Red and yellow buoy and create training,
validation and test data sets.

This file converts RGB to HSV using a built-in function.
"""

#### Libraries
# Third-party libraries
import numpy as np
import colorsys

def load_data():
    # Load the data for red_buoy and yellow buoy

    red_buoy = np.array([1,0,0])
    yellow_buoy = np.array([0,1,0])
    water = np.array([0,0,1])


    red_buoy_data = open("Data/filtered_red_data.txt",'r').readlines()
    yellow_buoy_data = open("Data/filtered_yellow_data.txt",'r').readlines()
    water_data = open("Data/filtered_water_data.txt",'r').readlines()
    # red_buoy_data.close()
    # yellow_buoy_data.close()
    # water_data.close()

    file_list = [red_buoy_data, yellow_buoy_data, water_data]

    RelatedTo = [red_buoy, yellow_buoy, water]

    RYWData = []

    for counter, file_data in enumerate(file_list):

        for line in file_data:

            B, G, R = [float(y) / 256.0 for y in line.split()]

            H, S, V = colorsys.rgb_to_hsv(R, G, B)

            # H    -> fraction of 360 degrees
            # S, V -> fraction <= 1

            # print "%0.2f %0.2f %0.2f -> %0.2f %0.2f %0.2f" %(R, G, B, H, S, V)
            
            RYWData.append([[H, S, V], RelatedTo[counter]])

    # print len(RYWData)
    # print RYWData[-1]
    # print np.shape(RYWData)

    # print np.shape(Rdata)
    # print np.shape(Ydata)
    # print np.shape(data)

    np.random.shuffle(RYWData) # Random shuffling of yellow and red buoy

    N = int(len(RYWData)*0.70)
    V = int(len(RYWData)*0.15)
    T = len(RYWData) - N -V

    # print N, V, T

    training_data = RYWData[0:N]
    validation_data = RYWData[N:N+V]
    test_data = RYWData[N+V:N+V+T]

    return (training_data, validation_data, test_data)
