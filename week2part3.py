# ...........................................................................
# Matplotlib and Pyplot
# ...........................................................................

# More info https://www.w3schools.com/python/matplotlib_plotting.asp
# Matplotlib is a Python plotting library that produces
# publication-quality figures.

import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,3,6,16])
# plt.show()

# plotting function with two arguments

# x = np.linspace(0,10,20)
# y = x**2
# plt.plot(x,y)
# plt.show()

# Using linewidth and makerspace......

# We can also provide a third argument to the plot function, which is a format
# string that specifies color, marker, and line type
# Letters and symbols of the format string are the same as in Matlab,
# x = np.linspace(0,10,20)
# y1 = x**2.0
# y2 = x**1.5
# plt.plot(x,y1,'bo-',linewidth = 2, markersize = 4)
# plt.show()

# plt.plot([0,1,2],[0,1,4],"rd-")
# plt.show()

# ...........................................................................
# Customising PLots - labels, legend
# ...........................................................................

# plt.axis([xmin, xmax, ymin, ymax])
# x = np.linspace(0,10,20)
# y1 = x**2.0
# y2 = x**1.5
# plt.plot(x,y1,'bo-',linewidth = 2, markersize = 4,label = 'First')
# plt.plot(x,y2,'gs-',linewidth = 2, markersize = 4, label = 'Second')
# plt.xlabel('$X$')
# plt.ylabel('$Y$')
# plt.axis([-0.5,10.5,-5,105])
# plt.legend(loc='upper left')
# plt.savefig('myplot.png')
# plt.show()


# x = np.array([ [0,1,0],[1,0,1] ])
# y = [0,1,0]
# x = np.append(x,[y],axis=0)
# plt.matshow(x)
# plt.show()

# i = 1
# x = np.array( [0,1,0,1,0,1,0] )
# while i < 7:
#     i = i+1
#     if i%2 ==0:
#         a = np.array([ [1,0,1,0,1,0,1] ])
#     else:
#         a = np.array([ [0,1,0,1,0,1,0] ])
#     x = np.vstack([x,a])
# plt.matshow(x,cmap = 'bwr_r')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# i=1
# x=np.array([0,0,0,0,0,0,0])
# while i<7:
#     i=i+1
#     if i%2==0:
#         a=np.array([0,0,0,0,0,0,0])
#     else:
#         a=np.array([1,1,1,1,1,1,1])
#     x=np.vstack([x,a])
# plt.matshow(x)
# plt.show()

# Logartithmic plot.........

# x = np.logspace(-1,1,40) # starts at 10^-1 and ends at 10^1
# y1 = x**2
# y2 = x**3
# y3 = x**4
# plt.loglog(x,y1,label = 'x^2')
# plt.loglog(x,y2,label = 'x^3')
# plt.loglog(x,y3,label = 'x^4')
# plt.axis([-0.5,10.5,-5,105])
# plt.legend(loc='upper left')
# plt.show()

# Generating histograms.................

# x = np.random.normal(size=1000)
# y = np.random.normal(size=1000)
# plt.hist(x)
# plt.hist(y)
# plt.show()

# x = np.random.normal(size = 1000)
# plt.hist(x, bins=np.linspace(-5, 5, 21));
# plt.show()

# Using gamma distribution and subplots
# 2 rows 2 columns = 4 elements labelled 1 to 4
x = np.random.gamma(2, 3, 100000)
plt.figure()
plt.subplot(221)
plt.hist(x, bins = 30)
plt.subplot(222)
plt.hist(x, bins = 30, density=True, stacked=True)
plt.subplot(223)
plt.hist(x, bins = 30, cumulative = 30)
plt.subplot(224)
plt.hist(x, bins = 30, density=True, stacked=True, histtype = "step")
plt.show()
