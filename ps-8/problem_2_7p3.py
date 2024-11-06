import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pylab as pl


  
#load txt file  
piano = np.loadtxt("piano.txt",float)
trumpet = np.loadtxt("trumpet.txt",float)

#plot data
#plt.plot(piano)
#plt.plot(trumpet)
#plt.xlabel('time')
#plt.ylabel('amplitude')
#pl.show()
#plt.savefig('piano.png')
#plt.savefig('trumpet.png')

#calculate dft
p_dft = np.fft.ifft(piano)
t_dft = np.fft.ifft(trumpet)
plt.xlim(0,10000)

#plt.plot(p_dft.real)
plt.plot(t_dft.real)
pl.show()
plt.xlabel('frequency (hz)')
plt.ylabel('coefficient')
#plt.savefig('piano_ft.png')
plt.savefig('trumpet_ft.png')



