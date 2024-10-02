from gaussxw import gaussxw
import numpy as np
import math
import matplotlib.pyplot as plt



#define integrand function
def f(x):
 num=(x**4) * math.exp(x)
 den=(math.exp(x) -1)**2
 f= num / den 
 return f
 

#Part A
#define function that computes Cv for given T
def cv(T):
#define constants
 V = 0.001 #Volume of solid cubic meters
 theta_d = 428 #Debye temperature
 rho = 6.022e28 #number density of atoms
 kb = 1.38e-23 #Boltzmann's constant
 N = 50 #number of sample points
 a = 0 #int limit lower
 b = V/T  #int limit upper
 
 #calculate sample points and weights, map to integration domain
 x,w = gaussxw(N)
 xp = 0.5*(b-a)*x + 0.5*(b+a)
 wp = 0.5*(b-a)*w
# Perform the integration
 s = 0.0
 for k in range(N):
  s += wp[k]*f(xp[k])
  cv = (9*V*rho*kb*(T/theta_d)**3) * s 
# print("Cv: " +str(cv))
 return cv 

#Part B
#plot
xvals=np.arange(5,505,5)
print(xvals)
yvalslist=[]
for xval in xvals:
 yvalslist.append(cv(xval))
#yvals
yvals=np.array(yvalslist)

#make plot
plt.plot(xvals,yvals,c='black')
plt.xlabel('Temperature (K)')
plt.ylabel('Heat Capacity of Aluminum (J/K)')

#save plot as image
plt.savefig('problem1_heat_capacity.png')


 
 
 
 
