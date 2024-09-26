import numpy as np
import matplotlib.pyplot as plt
import timeit 

nset=[10,20,30,40,50,60,70,80,90,100]

tloop=[]
tdot=[]

for N in nset:

 timeloop=timeit.timeit('''
A=np.ones(['''+str(N)+','+str(N)+'''],float)
B=np.ones(['''+str(N)+','+str(N)+'''],float) 
C = np.zeros(['''+str(N)+','+str(N)+'''],float)
for i in range('''+str(N)+'''):
 for j in range('''+str(N)+'''):
  for k in range('''+str(N)+'''):
   C[i,j] += A[i,k]*B[k,j]
''',number=1,setup='import numpy as np')   
 timedot=timeit.timeit('''
A=np.ones(['''+str(N)+','+str(N)+'''],float)
B=np.ones(['''+str(N)+','+str(N)+'''],float)
D=np.dot(A,B)''',number=1,setup='import numpy as np')   

 tloop.append([timeloop])
 tdot.append([timedot])
 
 
print(tloop)
print(tdot) 
nsetarray=np.array(nset)
tlarray=np.array(tloop) 
tdarray=np.array(tdot)

plt.plot(nsetarray,tlarray,15,label='Loop method times')
plt.plot(nsetarray,tdarray,15,label='Dot method times')
plt.xlabel('Square Matrix Side Length')
plt.ylabel('Time of computation (s)')
plt.ylim(0,.75)
plt.legend()

#save plot as image
plt.savefig('timecompare.png')

