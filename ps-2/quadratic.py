
import numpy as np

def quadratic(a,b,c):

 x2 = np.divide((-b - np.sqrt(np.square(b)-4*a*c)),2*a)
 x1 = np.divide(2*c,(-b - np.sqrt(np.square(b)-4*a*c)))
 print(x1)
 print(x2)
 return x1,x2
