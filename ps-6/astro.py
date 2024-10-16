import numpy as np
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import scipy


#only 500 galaxies were used in the later parts due to memory problems with the full set



#Part A
#load data,
hdu_list = pyfits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data
#print(len(flux[1]))
#print(len(logwave))
print('flux')
print(flux)

#plot several galaxy spectra
#plt.scatter(logwave,flux[0],label='0')
#plt.scatter(logwave,flux[1],label='1')
#plt.scatter(logwave,flux[2],label='2')
#plt.scatter(logwave,flux[3],label='3')
#plt.scatter(logwave,flux[4],label='4')

#plt.xlabel('log wavelength')
#plt.ylabel('flux (10−17 erg s−1 cm−2 A−10)')
#plt.legend()

#plt.savefig('part_a.png')



#Part B

fluxnormint = np.empty(len(flux), dtype=object)
norm= np.empty(len(flux), dtype=object)
print('lennorm')
print(len(norm))
#fluxnormal= np.empty(len(flux), dtype=np.float64)
for n in range(len(flux)):
 fluxnormint[n]=flux[n]/scipy.integrate.simpson(flux[n], x=logwave)
 norm[n]=scipy.integrate.simpson(flux[n], x=logwave)
# fluxnormal[n]=flux[n]/sum(flux[n])


#print('flux')
#print(flux)
print('fluxnormint')
print(fluxnormint)



#print('fluxnormal')
#print(fluxnormal)

#print(scipy.integrate.simpson(fluxnormint[1], x=logwave))
#print(scipy.integrate.simpson(fluxnormint[2], x=logwave))
#print(scipy.integrate.simpson(fluxnormint[77], x=logwave))
#print(scipy.integrate.simpson(fluxnormint[7025], x=logwave))
#print(sum(fluxnormint[1]))
#print(sum(fluxnormint[2]))
#print(sum(fluxnormint[77]))
#print(sum(fluxnormint[7025]))

#Part C
#calculate mean and residuals
meanflux= np.empty(len(flux), dtype=np.float64)
for m in range(len(flux)):
 meanflux[m]= np.mean(fluxnormint[m])
print('meanflux')
print(meanflux)
print(len(meanflux))

#print(np.mean(fluxnormint[0]))
#print(np.mean(fluxnormint[1]))
#print(np.mean(fluxnormint[2]))
#print(np.mean(fluxnormint[4000]))
residual=fluxnormint-meanflux
print(residual)

#Part D
#create covariance matrix
#c_matrix= np.empty([len(flux),len(flux)], dtype=np.float64)
#for o in range(len(flux)):
# for p in range(len(flux)):
#  c_matrix[o,p]=np.dot(residual[o],residual[p])
  
R=np.empty([500,len(logwave)], dtype=np.float64)
#R=np.empty([len(flux),len(logwave)], dtype=np.float64)

for q in range(500):
#for q in range(len(flux)):
 R[q,:] = residual[q]
print(R)
print('size')
print(np.prod(R.shape))

RT=np.transpose(R)
print(RT)
C=np.dot(RT,R)

print('c_matrix')
print(C)
print('size c')
print(np.prod(C.shape))

eigval,eigvec=np.linalg.eig(C)
print('vec')
#eigvec.sort(axis=-1, kind=None, order=None)
print(eigvec)




plt.xlabel('component number')
plt.ylabel('component value')
plt.legend()

plt.savefig('part_d.png')

#Part E
(U, w, VT) = np.linalg.svd(R)
UT=np.matrix.transpose(U)
V=np.transpose(VT)
#V.sort(axis=-1, kind=None, order=None)
print('w')
print(w)

print('v')
print(V)
print('size')
print(np.prod(V.shape))
#plot first 5 eigenvectors
plt.scatter(np.arange(len(logwave)),eigvec[0,:],label='0')
plt.scatter(np.arange(len(logwave)),eigvec[1,:],label='1')
plt.scatter(np.arange(len(logwave)),eigvec[2,:],label='2')
plt.scatter(np.arange(len(logwave)),eigvec[3,:],label='3')
plt.scatter(np.arange(len(logwave)),eigvec[4,:],label='4')
#Part F

(Uc, wc, VTc) = np.linalg.svd(C)
print('W (C)')
print(wc)

print('c 5')
print(C[0:5,:])

#Part G
five_coeff_dot_eigvec= np.dot(C[0:500,],V)
mflux_fcde=meanflux[0:500]+five_coeff_dot_eigvec
norm_mf_fcde=np.empty([500,len(logwave)], dtype=np.float64)
for s in range(500):
 norm_mf_fcde[s,:]=norm[s]*mflux_fcde[s]
print('flix again')
print(norm_mf_fcde)
#Part H

plt.scatter(C[1,:],C[0,:],label='c0 vs c1')
plt.xlabel('c1')
plt.ylabel('c0')

plt.scatter(C[2,:],C[0,:],label='c0 vs c2')
plt.xlabel('c2')
plt.ylabel('c0')


#Part I
for n in range(20):







