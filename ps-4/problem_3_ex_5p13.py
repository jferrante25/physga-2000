from gaussxw import gaussxw
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy

#Part A

def H(n,x):
 Hn=[1,2*x]
 if n == 0:
  h = 1
 if n == 1:
  h = 2*x
 if n >1 :
  for m in range(2,n+1):
#   print(range(2,n+1))
   hm =2*x*Hn[m-1]-2*(m-1)*Hn[m-2]
   Hn.append(hm)
#   print(Hn)
 hn=Hn[n]
 return hn  

#plot
xvals=np.arange(-4,4.1,0.1) # Part A
#xvals=np.arange(-10,10.1,0.1) # Part B
#print(xvals)

def phi(n,x):
 phi= 1/math.sqrt(2**n*math.factorial(n)*math.sqrt(math.pi)) *math.exp((-(x**2)/(2)))*H(n,x)
 return phi
 
for n in range(0,4): # Part A
#thirty=[30]
#for n in thirty: # Part B
 yvalslist=[]
 for xval in xvals:
  yvalslist.append(phi(n,xval))

#yvals
 yvals=np.array(yvalslist)

#make plot
 plt.plot(xvals,yvals,label='n: '+str(n))
 plt.xlabel('X')
 plt.ylabel('Phi_n(x)')
 plt.legend()

#save plot as image
plt.savefig('qho_nth_wave_efunction.png') # Part A
#plt.savefig('qho_30th_wave_efunction.png') # Part B


#Part C
#define function that computes uncertainty for nth wave function
def uncert(n):
#define constants
 N = 100 #number of sample points
 a = -1.0 #int limit lower
 b = 1.0 #int limit upper
 
#define integrand function
 def f(x,n):
  return ((1+x**2)/((1-x**2)**2))*((x/(1-x**2))**2)*(phi(n,(x/(1-x**2))))**2

#calculate sample points and weights, map to integration domain
 x,w = gaussxw(N)
 xp = 0.5*(b-a)*x + 0.5*(b+a)
 wp = 0.5*(b-a)*w
# Perform the integration
 s = 0.0
 for k in range(N):
  s += wp[k]*f(xp[k],n)
  uncert = s 
 return uncert 
 
print('<x^2> for n=5')  
print(uncert(5))
print('sqrt<x^2> for n=5')  
print(math.sqrt(uncert(5)))


#Part D
#define function that computes uncertainty for nth wave function with Gauss Hermite quad.
def uncert2(n):
#define constants
 N = 100 #number of sample points
 a = -1.0 #int limit lower
 b = 1.0 #int limit upper
 
#define integrand function
 def f(x,n):
  return ((1+x**2)/((1-x**2)**2))*((x/(1-x**2))**2)*(phi(n,(x/(1-x**2))))**2

#calculate sample points and weights, map to integration domain
 x,w = scipy.special.roots_hermite(N, mu=False)
 xp = 0.5*(b-a)*x + 0.5*(b+a)
 wp = 0.5*(b-a)*w
# Perform the integration
 s = 0.0
 for k in range(N):
  s += wp[k]*f(xp[k],n)
  uncert2 = s 
 return uncert2 
 
print('GH quad <x^2> for n=5')  
print(uncert2(5))
print('GH quad sqrt<x^2> for n=5')  
print(math.sqrt(uncert2(5)))


