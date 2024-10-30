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



#define function and derivative


def func(x,Mval,mval,Rval):
    return(G*Mval/x**2 -G*mval/(Rval-x)**2 - x*(G*Mval/Rval**3))

def dfunc(x,Mval,mval,Rval):
    return(-2*G*Mval/x**3 -2*G*mval/(Rval-x)**3 - (G*Mval/Rval**3))
    
#define Newton's method implementation    
    
def newton_raphson(xst, Mval, mval,Rval):
 tol = .00001*Rval
 maxiter = 100
 x = xst
# plt.plot(xgrid, func(xgrid,Mval, mval,Rval))
# plt.plot(xgrid, 0. * func(xgrid,Mval, mval,Rval))
 for i in np.arange(maxiter):
  delta = - func(x,Mval,mval,Rval) / dfunc(x,Mval,mval,Rval)

  x = x + delta
  if(np.abs(delta) < tol):
   return(x)

moonearth=newton_raphson(R_earth_moon/5,M_earth,M_moon,R_earth_moon)
print("moon-earth L1:")
print(moonearth)
print("earth-sun L1:")
earthsun=newton_raphson(97*R_earth_sun/100,M_sun,M_earth,R_earth_sun)
print(earthsun)
print("jupiter mass-sun L1:")
jupsun=newton_raphson(R_earth_sun/8,M_sun,M_jupiter,R_earth_sun)            
print(jupsun)
            
          
    
    
  
