import numpy as np
import matplotlib.pyplot as plt
import functions as f
plt.ion()
pi = np.pi

def main():
    ## Setting up space and courant number c = u*(dt / dx)
    nx = 40	   # Number of points in space
    c = 0.2	   # the Courant number
    x = np.linspace(0, 1, nx+1)	# spatial variable, with 41 points
    nt = 40 	   # Number of timesteps
    u = 1.
    dx = 1./nx
    dt = c*dx/u
    
    t = nt*dt
    
    ## phi = dependent variable, two time levels of it needed
    phi = f.initial_bell(x)
    phiNew = phi.copy()
    
    p = f.FTBS(phi,phiNew)
    return p

if __name__=="__main__":
    main()
    
    
