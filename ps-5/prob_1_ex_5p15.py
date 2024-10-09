import numpy as np
import math
import matplotlib.pyplot as plt
import jax
import jax.numpy as jnp

#define user defined function
def f(x):
 return 1+ 0.5 *np.tanh(2*x)
 
#central difference
def diff_central(func=None, x=None, dx=None):
 return((func(x + 0.5 * dx) - func(x - 0.5 * dx)) / dx)
 
num = 10000
x = 4 * (np.arange(num, dtype=np.float64) + 0.5) / np.float64(num) -2
dfdx = diff_central(func=f, x=x, dx=0.5 * 1.e-5)

#plots
plt.plot(x, 1- (np.tanh(2*x))**2,label='analytic solution')
plt.plot(x, dfdx,label='central difference')
plt.xlabel('x')
plt.ylabel('df / dx')

#define function for Jax
def g(x):
 return 1+0.5*jnp.tanh(2*x)


#implement and plot Jax autodiff
dv_jax = jax.grad(g)
dv = jax.vmap(dv_jax)(x)  
plt.plot(x, dv, label='Jax autodiff method')
plt.legend()

#save plot as png
plt.savefig('prob_1.png')
