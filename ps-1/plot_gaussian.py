import numpy as np
import matplotlib.pyplot as plt

#define gaussian
x=np.linspace(-10,10,50)
y=np.divide(np.exp(-np.divide(np.square(x),18)),np.sqrt(18*np.pi))

#plot gaussian
plt.plot(x,y,15,c='black')
plt.ylim(0,.2)
plt.xlabel('X')
plt.ylabel('Y')

#save plot as image
plt.savefig('gaussian.png')
