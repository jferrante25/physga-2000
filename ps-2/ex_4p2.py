import numpy as np
import quadratic

def quad(a,b,c):
#part a
 x1 = np.divide((-b + np.sqrt(np.square(b)-4*a*c)),2*a)
 x2 = np.divide((-b - np.sqrt(np.square(b)-4*a*c)),2*a)
 
#part b 
 x3 = np.divide(2*c,(-b - np.sqrt(np.square(b)-4*a*c)))
 x4 = np.divide(2*c,(-b + np.sqrt(np.square(b)-4*a*c)))
 print(x1)
 print(x2)
 print(x3)
 print(x4)
 

quad(0.001,1000,0.001)
 
 
quadratic.quadratic(0.001,1000,0.001)


