"""
data_loader
~~~~~~~~~~~~

data_loader is the function usually called by our neural network
code to load the data of Red and yellow buoy and create training,
validation and test data sets.
"""

#### Libraries
# Third-party libraries
import numpy as np


def load_data():
    # Load the data for red_buoy and yellow buoy
    
    red = np.array([1,0])
    yellow = np.array([0,1])

    red_buoy = open("/home/aniket/Desktop/Priyank/filtered_train_data_red.txt",'r')
    yellow_buoy = open("/home/aniket/Desktop/Priyank/filtered_train_data_yellow.txt",'r')

    Rdata = []
    lines = red_buoy.readlines()
    for line in lines:
        Rdata.append( [[float(x)/256 for x in line.split()],red] )

    Ydata = []
    lines = yellow_buoy.readlines()
    for line in lines:
        Ydata.append( [[float(x)/256 for x in line.split()],yellow] )

    data = Rdata + Ydata
    red_buoy.close()
    yellow_buoy.close()

    # print np.shape(Rdata)
    # print np.shape(Ydata)
    # print np.shape(data)
    np.random.shuffle(data) # Random shuffling of yellow and red buoy
    N = int(len(data)*0.6)
    V = int(len(data)*0.2)
    T = len(data) - N -V

    # print N, V, T

    training_data = data[0:N]
    validation_data = data[N:N+V]
    test_data = data[N+V:N+V+T]


    return (training_data, validation_data, test_data)


   

