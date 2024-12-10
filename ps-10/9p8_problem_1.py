import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt
import banded


def init():
    line.set_data([], [])
    return (line,)


#Part A: Solving equation
#define constants
m= 9.19e-31
L = 1e-8 
N = 1000
hbar = 1.05457e-34
k = 5e10
sigma = 1e-10
h = 1e-18
x0=L/2
 
a = L/N

a1 = 1 + h * 1j *hbar/(2*m*a**2)
a2 = -h*1j*hbar/(4*m*a**2)

b1 = 1- h*1j*hbar/(2*m*a**2)
b2 = h * 1j*hbar/(4*m*a**2)

fig, ax = plt.subplots()

ax.set_xlim(( 0,L))
ax.set_ylim((- 1, 1))
plt.xlabel('x')
plt.ylabel('psi(x)')

line, = ax.plot([], [], lw=2)

nframes = 500
def init():
    line.set_data([], [])
    return (line,)


#set initial psi
xvals= np.arange(0,L+a,a)
psi0= np.exp(-(xvals-x0)**2 / (2*sigma**2)) *np.exp(1j *k*xvals)



#Define A matrix, B matrix 
A = np.zeros([N+1,N+1],complex)
B = np.zeros([N+1,N+1],complex)
for i in range(0,N+1):
 for j in range(0,N+1):
  if i == j:
   A[i][j]=a1
   B[i][j]=b1
  if i == j+1 or i==j-1:
   A[i][j]=a2
   B[i][j]=b2



def cranknicholstep(psi):
 v = np.matmul(B,psi)
 psinew = np.linalg.solve(A,v)
 return psinew

nstep = 3000
q = np.zeros((nstep, 1001),complex)
qreal = np.zeros((nstep, 1001),float)
q[0, :] = psi0
qreal[0,:]=np.real(psi0)

for i in np.arange(nstep - 1):
  q[i + 1, :] = cranknicholstep(q[i,:])
  qreal[i + 1, :] = np.real(q[i+1,:])

def frame(i):
    line.set_data(xvals, qreal[i, :])
    return (line,) 
 
#Part B: Animation
anim = animation.FuncAnimation(fig, frame, init_func=init,
                               frames=nstep, interval=40,
                               blit=True)

anim.save('prob_1.gif',writer='pillow')
#visual.display(x=100,y=100,width=600,height=600,center=[5,0,0],forward[0,0,-1],background=color.blue,foreground=color.yellow)
















