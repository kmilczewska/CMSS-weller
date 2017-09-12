## File of functions for FTBS and CTCS schemes.
import numpy as np
import matplotlib.pyplot as plt
wkdir='/home/v2518/climateModelling/numerics/'
plt.ion()
pi = np.pi

## Define the initial and analytic solution:
def initial_bell(x):
    return np.where(x%1. <0.5, np.power(np.sin(2*x*pi),2), 0)

def FTBS(x,u,t,nt,nx,dt,dx,p,pNew):
    """FTCS scheme for burgers equation """
    ## Loop over all timestps using FTBS:
    for n in xrange(nt):
        ## Loop over space
        for j in xrange(1,nx):
    	    pNew[j] = p[j] - ((dt/dx)*p[j])*(p[j]-p[j-1])
        ## Setup boundary conditions
        pNew[0] = p[0] - ((dt/dx)*p[0])*(p[0]-p[nx-1])
        pNew[nx] = pNew[0]

        p = pNew.copy()
        plot_solution(x,p,u,t,scheme='FTBS')

    return p

def CTCS(x,u,t,nt,nx,dt,dx,p,pNew,pOld):
    """
    CTCS scheme for burgers equation
    """
    ## First timestep using FTCS:
    for j in xrange(1,nx):
        pNew[j] = p[j] - (0.5*(dt/dx)*p[j])*(p[j+1] - p[j-1])
    pNew[0] = p[0] - (0.5*(dt/dx)*p[0])*(p[1] - p[nx-1])
    pNew[nx] = pNew[0]

    ## Loop over all other timesteps with CTCS:
    for n in xrange(nt):
        for j in xrange(1,nx):
            pNew[j] = pOld[j] - ((dt/dx)*p[j]*(p[j+1]-p[j-1]))
        pNew[0] = pOld[0] - ((dt/dx)*p[0]*(p[1]-p[nx-1]))
        pNew[nx] = pNew[0]
        pOld = p.copy()
        p = pNew.copy()
        plot_solution(x,p,u,t,scheme='CTCS')

    return p


def plot_solution(x,p,u,t,scheme=None):
    """Function to plot the solution """
    plt.figure(1)
    #plt.clf()
    
    if scheme=='FTBS':
        plt.plot(x, p, 'b', label='FTBS')
    elif scheme=='CTCS':
        plt.plot(x, p, 'r', label='CTCS')
    plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.axhline(0,linestyle=':',color='black')
    plt.savefig(wkdir+'/plots/burgers_test.png')
    plt.show()
    plt.pause(0.01)
    
