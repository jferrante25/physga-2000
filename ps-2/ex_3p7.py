import numpy as np
import matplotlib.pyplot as plt
from pylab import imshow,show



xset= np.linspace(-2,2,1)
yset= np.linspace(-2,2,1)




mandel=[]
for x in xset:
 for y in yset:
  z=0  
  count=0
  while count < 100:
   if np.absolute(z) < 2:  
    z=np.square(z)+ x + y *1j
    count = count + 1
    if count ==100:
     mandel.append([x,y])
 
mandelnp=np.array(mandel)     
print(mandelnp)     
imshow(mandelnp)
   
    
 
  
#print(xset)
#print(yset)

# take all c grid
#for each c in grid
