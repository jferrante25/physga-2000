import math
import numpy as np
import pylab
import matplotlib.pyplot as plt

#define constants
g=9.8
R=0.08
C=0.47 
rho=1.22
v= 100



def f(r,t,m):

 x = r[0]
 x2 = r[1]
 y = r[2]
 y2 = r[3]
 fx = x2
 fx2 = - np.pi * R**2 * rho * C /(2*m) *x2 *np.sqrt(x2**2 + y2**2) 
 fy = y2
 fy2 = -g - np.pi * R**2 * rho * C /(2*m) *y2 *np.sqrt(x2**2 + y2**2) 
 return np.array([fx,fx2,fy,fy2],float)
 
a = 0
b = 10
N = 1000
h = (b-a)/N


tpoints = np.arange(a,b,h)
xpoints1 = []
ypoints1 = []

xpoints5 = []
ypoints5 = []

xpoints10 = []
ypoints10 = []


r = np.array([0.0,v*np.cos(np.pi/6),0.0,v*np.sin(np.pi/6)],float)

for t in tpoints:
 xpoints1.append(r[0])
 ypoints1.append(r[2])
 k1 = h*f(r,t,1)
 k2 = h*f(r+0.5*k1, t+0.5*h,1)
 k3 = h*f(r+0.5*k2, t+0.5*h,1)
 k4 = h*f(r+k3,t+h,1)
 r += (k1+2*k2+2*k3+k4)/6
 
#Part B
pylab.plot(xpoints1,ypoints1,label='m = 1 kg')
pylab.xlabel("x (m)")
pylab.ylabel("y (m)")
#pylab.show() 
 

 
# Part C 
r = np.array([0.0,v*np.cos(np.pi/6),0.0,v*np.sin(np.pi/6)],float)  
for t in tpoints:
 xpoints5.append(r[0])
 ypoints5.append(r[2])
 k1 = h*f(r,t,5)
 k2 = h*f(r+0.5*k1, t+0.5*h,5)
 k3 = h*f(r+0.5*k2, t+0.5*h,5)
 k4 = h*f(r+k3,t+h,5)
 r += (k1+2*k2+2*k3+k4)/6

 
pylab.plot(xpoints5,ypoints5,label='m = 5 kg')


r = np.array([0.0,v*np.cos(np.pi/6),0.0,v*np.sin(np.pi/6)],float)  
for t in tpoints:
 xpoints10.append(r[0])
 ypoints10.append(r[2])
 k1 = h*f(r,t,10)
 k2 = h*f(r+0.5*k1, t+0.5*h,10)
 k3 = h*f(r+0.5*k2, t+0.5*h,10)
 k4 = h*f(r+k3,t+h,10)
 r += (k1+2*k2+2*k3+k4)/6

 
pylab.plot(xpoints10,ypoints10,label='m = 10 kg')
pylab.legend()


pylab.show()
