import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

#Read data

data=np.loadtxt('dow.txt',float)

#plot data
plt.plot(data,label='original data')
#pl.show()

#calculate coefficients with rfft
coeff = np.fft.rfft(data)
print(coeff)
print(data)
print(len(data))
print(len(coeff))

#set latter 90% of array to zeros
coeff[51:513]=0

print(coeff)


#calculate inverse Fourier transform
invcoeff = np.fft.irfft(coeff)
plt.plot(invcoeff,color='red',label='inverted coefficients')
plt.legend()
plt.xlabel('day')
plt.ylabel('daily closing value')
#pl.show()
plt.savefig('problem_3.png')

