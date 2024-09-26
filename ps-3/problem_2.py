import numpy as np
from pylab import plot,xlabel,ylabel,legend,show
import random

NBi213 = 10000 # Number of bismuth 213 atoms
NBi209 = 0  # Number of bismuth 209 atoms
NTl = 0     # Number of thallium atoms
NPb = 0     # Number of lead atoms
tauBi213 = 46*60 #half life of Bi 213 in seconds
tauTl = 2.2*60 # Half life of thallium in seconds
tauPb = 3.3*60 # Half life of lead in seconds

h = 1.0 # Size of time-step in seconds
pBi213 = 1 - 2**(-h/tauBi213) # # Probability of decay of Bi 213 to Pb in one step
pTl = 1 - 2**(-h/tauTl) # Probability of decay of Tl in one step
pPb = 1 - 2**(-h/tauPb) # Probability of decay of Pb in one step
pBitoPb = 0.9791 # Probability of decay of Bi 213 to Pb in one step

tmax = 20000 # Total time

# Lists of plot points
tpoints = np.arange(0.0,tmax,h)
Bi209points = []
Bi213points =[]
Tlpoints = []
Pbpoints = []

# Main loop
for t in tpoints:
 Bi209points.append(NBi209)
 Bi213points.append(NBi213)
 Tlpoints.append(NTl)
 Pbpoints.append(NPb)
 
 #Calculate the number of Pb atoms that decay
 decayPb = 0 
 for i in range(NPb):
  if random.random() <pPb:
   decayPb += 1
 NPb -= decayPb
 NBi209 += decayPb
  
 #Calculate the number of Tl atoms that decay
 decayTl = 0 
 for j in range(NTl):
  if random.random() <pTl:
   decayTl += 1
 NTl -= decayTl
 NPb += decayPb
  
 
 #Calculate Bi213
 decayBi213 = 0 
 decaytoPb = 0
 decaytoTl = 0 
 for k in range(NBi213):
  if random.random() <pBi213:
   decayBi213 += 1
 for l in range(decayBi213):
  if random.random() <pBitoPb:
   decaytoPb += 1
  else:
   decaytoTl +=1
 NBi213 -= decayBi213
 NTl += decaytoTl
 NPb += decayPb
 
#Make the graph
#plot(tpoints,Bi213points,label='Number of Bi 213 atoms')
plot(tpoints,Tlpoints,label='Number of Tl atoms')
plot(tpoints,Pbpoints,label='Number of Pb atoms')
#plot(tpoints,Bi209points,label='Number of Bi 209 atoms')
legend()
xlabel("Time (s)")
ylabel("Number of atoms")
show()


 
 
  


