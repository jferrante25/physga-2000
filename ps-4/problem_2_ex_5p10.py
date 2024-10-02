from gaussxw import gaussxw
import numpy as np
import math
import matplotlib.pyplot as plt

#Part B

#define function that computes period T for given given amplitude
def T(amp):
#define constants
 m = 1 #mass of particle
 N = 20 #number of sample points
 a = 0.0 #int limit lower
 b = amp  #int limit upper
 
#define integrand function
 def f(x,amp):
  return 1/math.sqrt(amp**4 - x**4)

#calculate sample points and weights, map to integration domain
 x,w = gaussxw(N)
 xp = 0.5*(b-a)*x + 0.5*(b+a)
 wp = 0.5*(b-a)*w
# Perform the integration
 s = 0.0
 for k in range(N):
  s += wp[k]*f(xp[k],amp)
  T = math.sqrt(8*m) * s 
# print("T: " +str(T))
 return T 


#plot
xvals=np.arange(.2,2.2,.1)
print(xvals)
yvalslist=[]
for xval in xvals:
 yvalslist.append(T(xval))
#yvals
yvals=np.array(yvalslist)

#make plot
plt.plot(xvals,yvals,c='black')
plt.xlabel('Amplitude (m)')
plt.ylabel('Period of oscillation (s)')

#save plot as image
plt.savefig('problem2_period.png')


