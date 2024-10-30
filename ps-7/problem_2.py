import numpy as np
import scipy as sp

#define function
def f(x):
 return ((x-0.3)**2)*np.exp(x)
 
   
#implement parabolic step

def parabolic_step(func=None, a=None, b=None, c=None):
#returns the minimum of the function as approximated by a parabola
 fa = func(a)
 fb = func(b)
 fc = func(c)
 denom = (b-a) * (fb -fc) - (b-c)*(fb-fa)
 numer = (b-a)**2 * (fb-fc)-(b-c)**2* (fb-fa)
 #if sinular, just return b
 if(np.abs(denom) <1.e-15):
  x=b
 else:
  x=b-0.5 * numer / denom
 return(x) 
 
 

# implement golden 
def golden(func=None, astart=None, bstart=None, cstart=None, tol=1.5e-9):
 a =astart
 b = bstart
 c=cstart
 gsection = (3. -np.sqrt(5))/2
 while(np.abs(c-a)>tol):
  if((b-a)>(c-b)):
   x=b
   b = b -gsection * (b-a)
  else:
   x= b + gsection * (c-b)
  fb = func(b)
  fx = func(x)
  if(fb <fx):
   c =x
  else:
   a=b
   b=x
   


#implement Brent's method
def brent(func=None, astart=None, bstart=None, cstart=None, tol=1.e-9, maxiter=40000):
 a = astart
 b = bstart
 c = cstart
 bold = b+2.* tol
 niter = 0
 n=-1
 #keep track of successive parabolic steps
 blist=[]
 # try parabolic
 while((np.abs(bold-b)>tol) & (niter < maxiter)):
  n += 1
  blist.append(b)
  bold = b
  
  b =  parabolic_step(func=func, a=a, b=b, c=c)
  # if conditions are met, switch to golden  
  if n > 1: 
   if blist[n-2] > blist[n] or b < a or b > c: #if parabolic step is greater than that before last, or outside of bracket, switch to golden
    golden(func=f, astart=a, bstart=b, cstart=c, tol=1.5e-9)
    break
  if(b < bold):
   c = bold   
  else:
   a = bold

 return(b)  




#scipy brent
print('scipy')
print(sp.optimize.brent(f,brack=(0,40)))
print(sp.optimize.brent(f,brack=(0,20)))
print(sp.optimize.brent(f,brack=(0,5)))
print(sp.optimize.brent(f,brack=(0,4)))
print(sp.optimize.brent(f,brack=(0,3)))
print(sp.optimize.brent(f,brack=(0,2)))
print(sp.optimize.brent(f,brack=(0,1)))
#implmented brent
print('impl')
print(brent(func=f,astart=0,bstart=20,cstart=40))
print(brent(func=f,astart=0,bstart=10,cstart=20))
print(brent(func=f,astart=0,bstart=2.5,cstart=5))
print(brent(func=f,astart=0,bstart=2,cstart=4))
print(brent(func=f,astart=0,bstart=1.5,cstart=3))
print(brent(func=f,astart=0,bstart=1,cstart=2))
print(brent(func=f,astart=0,bstart=.5,cstart=1))




