# ...........................................................................
# Randomness and Time
# ...........................................................................


# Simulating randomness...
import random
import numpy as np
import matplotlib.pyplot as plt

# random.choice(['H', 'T']) #generates H or T
# random.choice([1,2,3,4,5,6]) #Simulating dice or use range(1,7)
#
# # simulate 3 random die with different sides and pick a value from one of them
# # random choice function within another random choice function
# x = random.choice( random.choice([range(1,7),range(1,9), range(1,11)]) )
# print(x)

# Simulating dice rolls and plotting histogram...........

# dice = list()
#
# for i in range(10000):
#     dice.append(random.choice([1,2,3,4,5,6]))
#
# plt.hist(dice, bins = np.linspace(0.5,6.5,7), histtype='bar', ec='black')
# plt.show()

# Simulating the sum of 10 random die.....................

# ys = []
#
# for rep in range(100000):
#     y = 0
#     for k in range(10):
#         x = random.choice([1,2,3,4,5,6])
#         y = y + x
#     ys.append(y)
#
# plt.hist(ys, bins=np.linspace(5.5,60.5,100),ec='black')
# plt.show()

# Using numpy random module ...................

# Generates a number between 0 and 1
# x = np.random.random()
# print(x)
#
# # Generating an array of random numbers
# y = np.random.random(5)
# print(y)
#
# z = np.random.random((2,3))
# print(z)

# Generating numbers from the normal distribution (mean,standard deviation)
# a = np.random.normal(0,1,(5,2))
# print(a)

# Repeating 10 die experiement with np.random

# X = np.random.randint(1,7,(10000000,10))
#
# # axis = 0 sums over all the columns, axis = 1 sums over all the rows
# Y = np.sum(X, axis=1)
# plt.hist(Y,ec='black')
# plt.show()

# a = np.random.random((5,2,3))
# print(a)

# Measuring time in scripts....................

import time

# Gives current time
# start_time = time.process_time()
#
# X = np.random.randint(1,7,(10000000,10))
# Y = np.sum(X, axis=1)
#
# end_time = time.process_time()
#
# run_time = end_time - start_time
# print(run_time)

# Comparing numpy vs random module time

# start_time_random = time.process_time()
#
# ys = []
# for rep in range(100000):
#     y = 0
#     for k in range(10):
#         x = random.choice([1,2,3,4,5,6])
#         y = y + x
#     ys.append(y)
#
# end_time_random = time.process_time()
#
# random_time = end_time_random - start_time_random
#
# start_time_np = time.process_time()
#
# X = np.random.randint(1,7,(100000,10))
# Y = np.sum(X, axis=1)
#
# end_time_np = time.process_time()
#
# np_time = end_time_np - start_time_np
#
# print('Difference in time is: ', (random_time - np_time)/np_time * 100,'%' )


# Random Walks...........................
# position at anytime is x0 + sum of random displacements (delx)
# x1 = x0 + del(x1)
# x2 = x1 + del(x2) = x0 + del(x1) + del(x2)

# Displacements in x and y
X_0 = np.array([[0],[0]]) #starting position (0,0)
delta_X = np.random.normal(0,1,(2,5))
X = np.concatenate((X_0, np.cumsum(delta_X, axis=1)), axis =1)

plt.plot(X[0], X[1], "ro-")
plt.show()
