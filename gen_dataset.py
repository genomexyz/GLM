#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#setting
dataset_filename = 'dataset.dat'


dataset_array = open(dataset_filename).read().split('\n')[1:]
if dataset_array[-1] == '':
	dataset_array = dataset_array[:-1]
for i in range(len(dataset_array)):
	dataset_array[i] = dataset_array[i].split(',')
dataset_array = np.asarray(dataset_array).astype('float32')

#pick data where student pick general course
new_dataset = []
for i in range(len(dataset_array)):
	if dataset_array[i,1] == 2:
		new_dataset.append(dataset_array[i])
new_dataset = np.asarray(new_dataset)
print(new_dataset)


#plot
plt.scatter(new_dataset[:,2], new_dataset[:,0])
plt.xlabel("score in Math")
plt.ylabel("Number of Award")
plt.show()
