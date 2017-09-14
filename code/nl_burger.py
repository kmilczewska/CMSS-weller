import numpy as np
import matplotlib.pyplot as plt
import functions as f
plt.ion()
pi = np.pi

def main():
    ## Setting up space and courant number c = u*(dt / dx)
    nx = 40.	   # Number of points in space
    x = np.linspace(0, 1, nx+1)	# spatial variable, with 41 points
    dx = x / nx
    nt = 40. 	   # Number of timesteps
    t = 20.
    dt = t / nt
 
    ## u = dependent variable, two time levels of it needed
    u = f.initial_bell(x)
    uNew = u.copy()
    
    p = f.FTBS(u,uNew)
    return p

if __name__=="__main__":
    main()
    
    
