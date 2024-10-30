import numpy as np
import matplotlib.pyplot as plt

#Set up code for Newton's method
#define constants
G = 6.67e-11 # gravitational constant
M_earth = 5.972e24 # mass of the earth
M_moon = 7.348e22  # mass of the sun
M_sun = 1.989e30   # mass of the sun
M_jupiter = 1.898e27 # mass of jupiter 

R_earth_moon = 3.844e8 # distance between earth and moon
R_earth_sun = 1.4873e11 # distance between earth and sun

mprime_em= M_moon/M_earth
mprime_es= M_earth/M_sun
mprime_ej= M_jupiter/M_sun

#define function and derivative


def func(x,mprime):
    return(G*(1/x**2-2/x+1)-G*mprime - G*(x-2*x**2+x**3))

def dfunc(x,mprime):
    return(G*(-2/x**3+2/x**2) - G*(1-4*x+3*x**2))
    
#define Newton's method implementation    
    
def newton_raphson(xst, mprime):
 tol = .00001
 maxiter = 100
 x = xst

 for i in np.arange(maxiter):
  delta = - func(x,mprime) / dfunc(x,mprime)

  x = x + delta
  if(np.abs(delta) < tol):
   return(x)

moonearth=newton_raphson(.1,mprime_em)
print("moon-earth L1:")
print(R_earth_moon*moonearth)
print("earth-sun L1:")
earthsun=newton_raphson(.1,mprime_es)
print(R_earth_sun*earthsun)
print("jupiter mass-sun L1:")
jupsun=newton_raphson(.1,mprime_ej)       
print(R_earth_sun*jupsun)
            
          
    
    
  
