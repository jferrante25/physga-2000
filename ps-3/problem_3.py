import numpy as np
from pylab import plot,xlabel,ylabel,legend,show
import random

tau = 3.053*60

#create 1000 random numbers from uniform dist 0 to 1
z = np.random.random(size=1001)

#use transformation method to obtain nonuniform dist
x = -np.divide(tau,np.log(2))*np.log(1-z)

sortedx = np.sort(x) 

y=list(range(1001))
print(y)
y.sort(reverse=True)
print(y)
yarray=np.array(y)
print(yarray)

#Make the graph
plot(sortedx,yarray)
xlabel("Time (s)")
ylabel("Number of Tl atoms")
show()


