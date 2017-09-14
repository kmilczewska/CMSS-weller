## File of functions for FTBS and CTCS schemes.
import numpy as np
import matplotlib.pyplot as plt
wkdir='/home/v2518/climateModelling/numerics/'
plt.ion()
pi = np.pi

## Define the initial and analytic solution:
def initial_bell(x):
    return np.where(x%1. <0.5, np.power(np.sin(2*x*pi),2), 0)

def FTBS(x,t,nt,nx,dt,dx,p,pNew):
    """FTCS scheme for burgers equation. Upwind, non-conservative scheme. """
    print p
    ## Loop over all timestps using FTBS:
    for n in xrange(int(nt)-1):
        ## Loop over space
        for j in xrange(1,int(nx)):
            c = (dt/dx)*p[j]
    	    pNew[j] = p[j] - (c*(p[j]-p[j-1]))
        ## Setup boundary conditions
        pNew[0] = p[0] - ((dt/dx)*p[0])*(p[0]-p[int(nx)-1])
        pNew[int(nx)] = pNew[0]
        p = pNew.copy()
        plot_solution(x,p,t,n,nt,d=1.0,col='b',scheme='FTBS')

    for n in xrange(int(nt),int(nt)+1):
        ## Loop over space
        for j in xrange(1,int(nx)):
            c = (dt/dx)*p[j]
    	    pNew[j] = p[j] - (c*(p[j]-p[j-1]))
        ## Setup boundary conditions
        pNew[0] = p[0] - ((dt/dx)*p[0])*(p[0]-p[int(nx)-1])
        pNew[int(nx)] = pNew[0]
        p = pNew.copy()
        plot_solution(x,p,t,n,nt,d=3.0,col='k',scheme='FTBS')
    return p

def CTCS(x,t,nt,nx,dt,dx,p,pNew,pOld):
    """
    CTCS scheme for burgers equation
    """
    ## First timestep using FTCS:
    for j in xrange(1,int(nx)):
        c = (dt/dx)*p[j]
        pNew[j] = p[j] - (0.5*c)*(p[j+1] - p[j-1])
    pNew[0] = p[0] - (0.5*(dt/dx)*p[0])*(p[1] - p[int(nx)-1])
    pNew[int(nx)] = pNew[0]
    p = pNew.copy()
    #plot_solution(x,p,t,n,nt,d=1.0,scheme='CTCS')
    ## Loop over all other timesteps with CTCS:
    for n in xrange(1,int(nt)-1):
        for j in xrange(1,int(nx)):
            c = (dt/dx)*p[j]
            pNew[j] = pOld[j] - (c*(p[j+1]-p[j-1]))
        pNew[0] = pOld[0] - ((dt/dx)*p[0]*(p[1]-p[int(nx)-1]))
        pNew[int(nx)] = pNew[0]
        pOld = p.copy()
        p = pNew.copy()
        plot_solution(x,p,t,n,nt,d=1.0,col='r',scheme='CTCS')

    for n in xrange(int(nt),int(nt)+1):
        for j in xrange(1,int(nx)):
            c = (dt/dx)*p[j]
            pNew[j] = pOld[j] - (c*(p[j+1]-p[j-1]))
        pNew[0] = pOld[0] - ((dt/dx)*p[0]*(p[1]-p[int(nx)-1]))
        pNew[int(nx)] = pNew[0]
        pOld = p.copy()
        p = pNew.copy()
        plot_solution(x,p,t,n,nt,d=3.0,col='k',scheme='CTCS')
    return p

def lax_wendroff(x,t,nt,nx,dt,dx,p,pNew):
    """
    Lax-Wendroff scheme. Second order, nonlinear conservation
    """
    def a(p,j):
        return (0.5*((p[j+1])**2) - 0.5*(p[j-1])**2 )
    def b(p,j):
        return 0.5*(p[j]+p[j+1])*(0.5*((p[j+1])**2) - 0.5*((p[j])**2))
    def c(p,j):
        return 0.5*(p[j]+p[j-1])*(0.5*((p[j])**2) - 0.5*(p[j-1])**2)

    for n in xrange(int(nt)-1):
        for j in xrange(int(nx)):
            pNew[j] = p[j] - (dt/(2*dx))*a(p,j) + ((dt**2)/(2*(dx**2)))*(b(p,j)-c(p,j))
        pNew[0] = p[0] - (dt/(2*dx))*a(p,0) + ((dt**2)/(2*(dx**2)))*(b(p,0)-c(p,0))
        pNew[int(nx)] = pNew[0]
        pOld = p.copy()
        p = pNew.copy()
        plot_solution(x,p,t,n,nt,d=1.0,col='g',scheme='Lax-Wendroff')

    for n in xrange(int(nt),int(nt)+1):
        for j in xrange(int(nx)):
            pNew[j] = p[j] - (dt/(2*dx))*a(p,j) + ((dt**2)/(2*(dx**2)))*(b(p,j)-c(p,j))
        pNew[0] = p[0] - (dt/(2*dx))*a(p,0) + ((dt**2)/(2*(dx**2)))*(b(p,0)-c(p,0))
        pNew[int(nx)] = pNew[0]
        pOld = p.copy()
        p = pNew.copy()
        plot_solution(x,p,t,n,nt,d=3.0,col='k',scheme='Lax-Wendroff')

    return p

def plot_solution(x,p,t,n,nt,d,col='None',scheme='None'):
    """Function to plot the solution """
    plt.figure(1)
    #plt.clf()
    
    if scheme=='FTBS':
        plt.plot(x, p, str(col), label='FTBS', linewidth=str(d))
        #plt.legend(loc='best')
        plt.ylim(ymax=1.0)
    elif scheme=='CTCS':
        plt.plot(x, p, str(col), label='CTCS', linewidth=str(d))
        #plt.legend(loc='best')
        plt.ylim(ymax=3.0)
    elif scheme=='Lax-Wendroff':
        plt.plot(x, p, str(col), label='Lax-Wendroff',linewidth=str(d))
        plt.ylim(ymax=2.0)
    #plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('$u(x,t)$')
    plt.axhline(0,linestyle=':',color='black')
    plt.title('t = %f' % (n))
    plt.savefig(wkdir+'/plots/burgers_'+str(scheme)+'_'+'nt=%s.png' % (nt))
    plt.show()
    plt.pause(0.01)

#def plots_sub(x,p,t
    
