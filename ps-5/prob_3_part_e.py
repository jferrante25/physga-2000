import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


data=np.genfromtxt("signal.dat",delimiter="|",skip_header=1,usecols=(1,2))
t=data[:,0]
s=data[:,1]



tp = (t - t.mean()) / t.std()
plt.scatter(tp,s)
plt.xlabel('time ')
plt.ylabel('signal')

#set period
p=(max(tp)-min(tp))/2
print(p)

A = np.zeros((len(tp),11))

A[:, 0] = 1.
A[:, 1] = np.sin(2*np.pi*tp/p )
A[:, 2] = np.cos(2*np.pi*tp/p )
A[:, 3] = np.sin(2*np.pi*2*tp/p )
A[:, 4] = np.cos(2*np.pi*2*tp/p )
A[:, 5] = np.sin(2*np.pi*3*tp/p )
A[:, 6] = np.cos(2*np.pi*3*tp/p )
A[:, 7] = np.sin(2*np.pi*4*tp/p )
A[:, 8] = np.cos(2*np.pi*4*tp/p )
A[:, 9] = np.sin(2*np.pi*5*tp/p )
A[:, 10] = np.cos(2*np.pi*5*tp/p )

print(A.shape)
print(A)

(u, w, vt) = np.linalg.svd(A, full_matrices=False)
print(u.shape)
print(w.shape)
print(vt.shape)
print(w)

ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = ainv.dot(s)
print(x)

sm = A.dot(x)
plt.plot(tp, s, '.', label='data')
plt.plot(tp, sm, '.', label='model (sinusoidal harmonic sequence up n=5)')
plt.xlabel('time')
plt.ylabel('signal')
plt.legend()

plt.savefig('prob_3_part_e.png')

