# ...........................................................................
# Numpy arrays
# ...........................................................................

# Making vectors and matrices
import numpy as np

# # Zero vectors
# zero_vector = np.zeros(3)
# print(zero_vector)
#
# zero_matrix = np.zeros( (3,4) )
# print(zero_matrix)
#
# # Identity matrices
# identity_matrix = np.ones( (3,3) )
# print(identity_matrix)

# Arrays

# x = np.array([1,2,3])
# print(x)

# y = np.array([ [1,2],[3,4] ])
# print(y)
#
# # Transpose function
# print(y.transpose())

# ...........................................................................
# Slicing and Indexing arrays
# ...........................................................................

# x = np.array([1,2,3])
# y = np.array([4,5,6])
# z = x + y #element wise addition
# print(x,y,z)
#
# print(x[2])
# print(x[0:2])

#2d arrays

# X = np.array([ [1,2,3],[4,5,6] ])
# Y = np.ones((2,3))
# print(X[0,1]) # corresponds to 1st row 2nd column
#
# Z = X[1,:] + Y[1,:]
# print(Z)

# indexing arrays with arrays - numpy array or regular lists
# z1 = np.array([1,2,3,4,5,6,7])
# z2 = z1 + 1
# print(z1,z2)
#
# index = [1,2,3]
# print(z2[index])
# print(z2[np.array(index)])

# Boolean arrays....
# print(z2>6)
# print(z2[z2>6])
# or this
# print(z2 > 6)
# print(z1[z2>6] ) #indexing z1 with elements from z2>6

# Slicing vs Indexing
# When you slice an array using the colon operator, you get a view of the object
# This means that if you modify it, the original array will also be modified.
# This is in contrast with what happens when you index an array, in which case
# what is returned to you is a copy of the original data.

# z1 = np.array([1,2,3,4,5])
# w = z1[:]
# z1[0] = 10
# print(z1,w)

# z2 = np.array([1,2,3])
# index = [0,1,2]
# w = z2[[0,1,2]]
# w[0] = 10
# print(z2,w)

# ...........................................................................
# Linspace, Logspace, dimensions, checking elements
# ...........................................................................

# Using the linspace command to construct an array of linearly spaced elements
# End point is included in the array in numpy
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# num is the number of points generated

# print(np.linspace(0,100,11))
#
# # In linear space, the sequence starts at base ** start (base to the power
# # of start) and ends with base ** stop
#
# # e.g. start at 10 (log10 =1) and end at 100 (log100 = 2)
# print(np.logspace(1,2,10))
#
# # e.g. generate log points between 250 and 500
# print( np.logspace(np.log10(250),np.log10(500),10) )

# Shapes (dimension) of an array
# X = np.array([ [1,2,3],[4,5,6] ])
# print(X.shape)
#
# # Size or elements in an array
# print(X.size)

# shape and size are data attributes, not methods of the arrays and have no ()

# Checking elements
# x = np.random.random(10) #generates 10 random numbers between 0 and 1
# print(np.any(x>0.1))
# print(np.all(x >= 0.1))

# x%i == 0 tests if x has a remainder when divided by i. If this is not true
# for all values strictly between 1 and x, it must be prime!

for x in range(2,11):
    print(x,not np.any([x%i == 0 for i in range(2, x)]))
