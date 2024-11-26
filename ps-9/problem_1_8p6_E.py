import math
import numpy as np
import pylab
import matplotlib.pyplot as plt

def f(r,t):
 omega = 1
 #mu = 1
 #mu = 2
 mu = 4
 x = r[0]
 y = r[1]
 fx = y
 fy = -omega**2 *x + mu*(1-x**2)*y
 return np.array([fx,fy],float)
 
a = 0
b = 20
N = 10000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
ypoints = []

r = np.array([1.0,0.0],float)

for t in tpoints:
 xpoints.append(r[0])
 ypoints.append(r[1])
 k1 = h*f(r,t)
 k2 = h*f(r+0.5*k1, t+0.5*h)
 k3 = h*f(r+0.5*k2, t+0.5*h)
 k4 = h*f(r+k3,t+h)
 r += (k1+2*k2+2*k3+k4)/6


#Phase plots
pylab.plot(xpoints,ypoints)
pylab.xlabel("x (m)")
pylab.ylabel("velocity (m/s)")

pylab.show()
