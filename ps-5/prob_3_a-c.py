import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


data=np.genfromtxt("signal.dat",delimiter="|",skip_header=1,usecols=(1,2))
t=data[:,0]
s=data[:,1]
#Part A
#plt.scatter(t,s)
#plt.xlabel('time')
#plt.ylabel('signal')
#plt.savefig('prob_3_part_a.png')

#Part B
tp = (t - t.mean()) / t.std()
#plt.scatter(tp,s)

A = np.zeros((len(tp),4))

A[:, 0] = 1.
A[:, 1] = tp 
A[:, 2] = tp**2
A[:, 3] = tp**3


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
#plt.plot(tp, s, '.', label='data')
#plt.plot(tp, sm, '.', label='model (3rd order polynomial)')
#plt.xlabel('time')
#plt.ylabel('signal')
#plt.legend()

#plt.savefig('prob_3_part_b.png')

#Part C
res = sm-s
plt.scatter(tp,res)
plt.xlabel('time')
plt.ylabel('signal-model residual')
plt.savefig('prob_3_part_c.png')


