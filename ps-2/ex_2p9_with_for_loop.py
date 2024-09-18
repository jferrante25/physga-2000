import numpy as np
import timeit

# for loop method
m = 0
for i in range(-100,101):
 for j in range(-100,101):
  for k in range(-100,101):
   if i == j == k == 0:
    continue
   if (i + j + k) % 2 == 0:
    m = m + np.divide(1,np.sqrt(np.square(i)+np.square(j)+np.square(k)))
   else: 
    m = m - np.divide(1,np.sqrt(np.square(i)+np.square(j)+np.square(k)))

print('Madelung constant: ' + str(m)) 
    

