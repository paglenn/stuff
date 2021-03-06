# Python modules
import numpy as np
import matplotlib.pyplot as pp
# User - defined
global N, R, V

###########################
#Parameters
d = 2 # dimension
N = 4 # num particles
dt = 0.001
Tf  = 2
a = LatticeSpacing = 2
dr = 0.001
L = LatticeRange = 20
numSteps = int(Tf/dt)
eps = 1. ; sigma = 1.  # lennard-Jones parameters
cutoff = 3.			# distance cutoff for pair interaction
m = np.ones(N) # mass of particles
gridX = np.linspace(0,L,int(L/a)+1)
dx = 0.5
v0 = 10. #set initial temperature
R = np.zeros((N,numSteps+1,d))
V = np.zeros((N,numSteps+1,d))
E = np.zeros(numSteps+1)


###########################
#Particles
# initial positions
goodSetup = 0

while goodSetup == 0:
	goodSetup = 1
	for i in range(N):

		# choose particle position in grid
		R0 = np.random.choice(gridX,d)
		R0 += (2*np.random.rand(d) - 0.5*np.ones(d)) * dx

		for pos in R[:,0]:
			if np.linalg.norm(R0-pos) < sigma:
				goodSetup = 0

		if goodSetup == 0: break
		else: R[i][0] = R0

for i in range(N):
	V[i,0] = v0 * 2*(np.random.rand(d) - 0.5*np.ones(d) )
R[:,1] = R[:,0] + V[:,0]*dt

#############################
# Functions for simulation
def occupied_sites(n):
	global R
	sites = list()
	for pvec in R[:,n,:]:
		sites.append(pvec)
	return sites

def U(r):
	# Lennard-Jones 6-12 potential function
	return 4*eps*((sigma/r)**12.- (sigma/r)**6.)

def F(i,n):
	global R,V
	Fi = np.zeros(d)
	sites = occupied_sites(n)
	ipos = sites[i]
	if i != N-1:
		otherSites = sites[:i] + sites[i+1:]
	else:
		otherSites = sites[:i]
	for site in otherSites:
		r1 = np.linalg.norm(ipos - site)
		r2 = np.linalg.norm(ipos + L*np.ones(d) - site)
		r = min([r1,r2])
		if r < cutoff:
			Fi += - (U(r + dr) - U(r - dr) ) /(2* dr)
	return Fi

def verlet_step(n):
	# computes new positions and velocities for time step n+1
	global R,V

	for i in range(N):
		a = F(i,n) / m[i]
		R[i][n+1] = 2*R[i][n] - R[i][n-1] + a * (dt**2.)
		V[i][n] = ( R[i][n+1] - R[i][n-1]) / (2*dt)


	# Periodic Boundary Conditions
	for i in range(N):
		for j in range(d):
			while R[i][n+1][j] > L:
				R[i][n+1][j]  -= L
				R[i][n][j] -= L
			while R[i][n+1][j] < 0:
				R[i][n+1][j]  += L
				R[i][n][j] -= L

def energy(n):
	KE = 0
	for i in range(N):
		KE += m[i] * np.linalg.norm(V[i,n])**2.

	PE = 0
	for i in range(N):
		for j in range(i+1,N):
			r =np.linalg.norm(R[i,n] - R[j,n])
			if r < cutoff:
				PE += U(r)
	PE = PE/2.
	return float(KE)/N


################################
# Simulation loop
for n in range(1,numSteps):
	verlet_step(n)
	E[n] = energy(n)


# Plot energy vs time
#pp.plot(np.linspace(0,Tf,numSteps),E[1:],'.')
#pp.ylim(0,500)
#pp.show()


