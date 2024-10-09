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

#Part D
A = np.zeros((len(tp),30))


for n in range(30):
 A[:, n] = 1. *tp**n

print(A.shape)
print(A)

(u, w, vt) = np.linalg.svd(A, full_matrices=False)
print(u.shape)
print(w.shape)
print(vt.shape)
print(w)

ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = ainv.dot(s)
#print(x)

sm = A.dot(x)
plt.plot(tp, s, '.', label='data')
plt.plot(tp, sm, '.', label='model (30th order polynomial)')
plt.xlabel('time')
plt.ylabel('signal')
plt.legend()

plt.savefig('prob_3_part_d.png')

