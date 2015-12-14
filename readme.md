# Task Buoy using Machine Learning

### Command to concat the files together:

```shell
cat main_0-51.txt main_51-61.txt main_61-71.txt main_71-81.txt main_81-101.txt main_101-121.txt main_121-141.txt main_141-161.txt main_161-200.txt main_200-256.txt > final_stored_array_rgb.txt
```

### Command to build the training CPP file

```shell
g++ `pkg-config opencv --cflags` buoy_train.cpp `pkg-config opencv --libs
```

### Command to run the executable generated from above command

```shell
./a.out path/to/video.avi path/to/output/text/file.txt
```
