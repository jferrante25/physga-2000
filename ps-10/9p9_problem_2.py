import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt
import dcst


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
xvals= np.arange(0,L,a)
psi0=np.exp(-(xvals-x0)**2 / (2*sigma**2)) *np.exp(1j *k*xvals)

#take real and imag poarts
realpsi  = np.real(psi0)
imagpsi  = np.imag(psi0)

#Fourier transform
rdst=  dcst.dst(realpsi) #a
idst=  dcst.dst(imagpsi) #eta


def spect(t):
 repsi = np.zeros(1000)
 invcoeff=np.zeros(1000)
 for j in range(999):
  invcoeff[j]=(rdst[j]*np.cos(np.pi**2 * hbar *(j+1)**2*t/(2*m*L**2))+idst[j]*np.sin(np.pi**2 * hbar*(j+1)**2*t/(2*m*L**2)))
 psi=dcst.idst(invcoeff)
 return psi

nstep = 3000
q = np.zeros((nstep, 1000),complex)
qreal = np.zeros((nstep, 1000),float)
q[0, :] = psi0
qreal[0,:]=np.real(psi0)

plt.plot(xvals,spect(1e-16))
plt.show()
for i in np.arange(nstep - 1):
 q[i, :] = spect(h*i)


def frame(i):
 line.set_data(xvals, q[i, :])
 return (line,) 
 
#Part B: Animation
anim = animation.FuncAnimation(fig, frame, init_func=init,
                               frames=nstep, interval=40,
                               blit=True)

anim.save('prob_2.gif',writer='pillow')
















