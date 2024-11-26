import math
import numpy as np
import pylab
import matplotlib.pyplot as plt

def f(r,t):
 omega=1
 x = r[0]
 y = r[1]
 fx = y
 fy = -omega**2 *x**3
 return np.array([fx,fy],float)
 
a = 0
b = 50
N = 1000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
ypoints = []

#r for part C (initial x value = 1)
#r = np.array([1.0,0],float)
#r for part C increased amp (initial x value = 2)
r = np.array([2.0,0],float)

for t in tpoints:
 xpoints.append(r[0])
 ypoints.append(r[1])
 k1 = h*f(r,t)
 k2 = h*f(r+0.5*k1, t+0.5*h)
 k3 = h*f(r+0.5*k2, t+0.5*h)
 k4 = h*f(r+k3,t+h)
 r += (k1+2*k2+2*k3+k4)/6

#Part C plots 
#pylab.plot(tpoints,xpoints)
#pylab.xlabel("t (s)")
#pylab.ylabel("x (m)")

#Part D plots
pylab.plot(xpoints,ypoints)
pylab.xlabel("x (m)")
pylab.ylabel("velocity (m/s)")

pylab.show()
