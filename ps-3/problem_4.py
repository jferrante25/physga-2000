import numpy as np
from pylab import plot,xlabel,ylabel,legend,show
import matplotlib.pyplot as plt


ylist=[]
for i in range(10000):
 x=np.random.exponential(scale=1.0, size=1000)
 yi=np.divide(1,len(x))*sum(x)
 ylist.append(yi)
 
#make and save plot 
y=np.array(ylist)
plt.hist(y, bins=100)
plt.xlabel('Y')
plt.ylabel('Number of Entries')
plt.savefig('dist.png')
