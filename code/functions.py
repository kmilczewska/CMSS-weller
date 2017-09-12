## File of functions for FTBS and CTCS schemes.
import numpy as np
import matplotlib.pyplot as plt
wkdir='/home/v2518/climateModelling/numerics/'
plt.ion()
pi = np.pi

## Define the initial and analytic solution:
def initial_bell(x):
    return np.where(x%1. <0.5, np.power(np.sin(2*x*pi),2), 0)

def FTBS(nt,nx,dt,dx,phi,phiNew):
    """FTCS scheme for burgers equation """
    ## Loop over all timestps using FTCS:
    for n in xrange(nt):
        ## Loop over space
        for j in xrange(1,nx):
    	    phiNew[j] = phi[j] - ((dt/dx)*phi[j])*(phi[j]-phi[j-1])
        ## Setup boundary conditions
        phiNew[0] = phi[0] - ((dt/dx)*phi[0])*(phi[0]-phi[nx-1])
        phiNew[nx] = phiNew[0]

        phi = phiNew.copy()
        plot_solution(phi)

    return phi


def plot_solution(p):
    """Function to plot the solution """
    plt.figure(1)
    #plt.clf()
    
    plt.plot(x, initial_bell(x - u*t), 'k', label='analytics')
    plt.plot(x, p, 'b', label='FTBS')
    #plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.axhline(0,linestyle=':',color='black')
    plt.savefig(wkdir+'/plots/burgers.png')
    plt.show()
    plt.pause(0.01)
