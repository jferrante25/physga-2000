import numpy as np
import jax 
import jax.numpy as jnp
import jax.scipy.optimize
import scipy.optimize as optimize
import matplotlib.pyplot as plt
import pylab as pl
import pandas as pd
jax.config.update("jax_enable_x64", True)

#load data
df= pd.read_csv('survey.csv')

#print(data.head())
#print(df['age'])
#print(df['recognized_it'])

#put data in np a
age=np.array(df['age'])
ri = np.array(df['recognized_it'])

#print(age)
#print(ri)


#define model
def prob(x, params=[None,None]):
 B0 = params[0]
 B1 = params[1]
 m = 1/(1+ jnp.exp(-(B0 + B1 *x)))
 return(m)

plt.scatter(age,ri,label='data')
plt.scatter(age,prob(age,[-4500,100]),color='red',label='example fit')
plt.legend()
plt.xlabel('age (years)')
plt.ylabel('answer (1:yes, 0:no)')
plt.savefig('problem_1_a.png')
#pl.show()

#define negloglike
def negloglike(params, *args):
 age = args[0]
 ri = args[1]
 B0= params[0]
 B1 = params[1]
 params2 = [B0,B1]
 p = prob(age, params=params2)
# likelihood each value is p(age) if ri =1 , 1-p(age) if ri=0
 lhood=1.0-ri + ((-1.0)**(ri-1.0))*(p)
 #-log likelihood of whole data set = - sum of log of each element
 ln_lhood=jnp.log(lhood)  
 nll = - ln_lhood.sum()
 return(nll)


#def negloglike grad
negloglike_grad = jax.grad(negloglike)


#optimze
pst = np.array([-4500, 100])
fit_params = optimize.minimize(negloglike, pst, args=(age, ri), jac=negloglike_grad,method='BFGS', tol=1e-06)
print(fit_params)
B0=fit_params[0]
B1=fit_params[1]
print(B0)
print(B1)



#def Hessian
#def hessian(f):
#  return jax.jacfwd(jax.grad(f))

#take negloglike hessian
#h = hessian(negloglike)
#hmat= np.array(h(B0,B1,age,ri))
#covar=np.linalg.inv(hmat)
#print(covar)















