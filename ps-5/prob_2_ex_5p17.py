import numpy as np
import math
import matplotlib.pyplot as plt
from gaussxw import gaussxw

#Part A
xval=np.arange(0.1,5.1,0.1)
for a in [2,3,4]:
 yval=np.exp(-xval)*xval**(a-1) 
 plt.plot(xval,yval,label=str(a)+' using old expression')
 plt.xlabel('x')
 plt.ylabel('y')

#Part D

xval2=np.arange(0.1,5.1,0.1)
for a in [2,3,4]:
 yval2=np.exp((a-1)*np.log(xval2)-xval2)
 plt.plot(xval2,yval2,label=str(a)+' using new expression')
 plt.xlabel('x')
 plt.ylabel('y')
plt.legend()


plt.savefig('prob_2.png') 

#Part E, integrate to compute gamma
def gamma(a):
#define constants
 N = 50 #number of sample points
 l = 0.000 #int limit lower
 u = 1.0 #int limit upper
 
#define integrand function with substition
 def f(x,a):
  return ((a-1)/((1-x)**2)) *np.exp((a-1)*np.log((a-1)*x/(1-x))-((a-1)*x/(1-x)))

#calculate sample points and weights, map to integration domain
 x,w = gaussxw(N)
 xp = 0.5*(u-l)*x + 0.5*(u+l)
 wp = 0.5*(u-l)*w 
# Perform the integration
 s = 0.0
 for k in range(N):
  s += wp[k]*f(xp[k],a)
 return s
 
print('gamma(3/2) = '+str(gamma(1.5)))


#Part F
print('gamma(3) = '+str(gamma(3)))
print('gamma(6) = '+str(gamma(6)))
print('gamma(10) = '+str(gamma(10)))


