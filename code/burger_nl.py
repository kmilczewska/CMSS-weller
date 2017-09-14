## CMSS Numerical Methods exercises with Hillary Weller
## Kaja Milczewska 14/09/17 Cambridge 
## k.m.milczewska@pgr.reading.ac.uk 
## Main script to solve non-linear burgers equation 
## via FTBS, CTCS and Lax-Wendroff

import numpy as np
import matplotlib.pyplot as plt
import functions as f


def main():
    """
    Function to solve the non-linear Burgers equation, u_t + uu_x = 0 (inviscid).
    """
    nx = 40.	   # Number of points in space
    x = np.linspace(0, 1, nx+1)	# spatial variable, with 41 points
    dx = 1. / nx
    nt = 100. 	   # Number of timesteps
    t = 1.
    dt = t / nt

    
    ## u = dependent variable, three time levels needed.
    u = f.initial_bell(x)
    uNew = u.copy()
    uOld = u.copy()
    
    ## Run schemes
    #p_F = f.FTBS(x,t,50,nx,dt,dx,u,uNew)
    #p_C = f.CTCS(x,t,50,nx,dt,dx,u,uNew,uOld)
    p_LW = f.lax_wendroff(x,t,300,nx,dt,dx,u,uNew)


    #f.plot_solution(x,p_F,t,scheme='FTBS')
    #f.plot_solution(x,p_C,t,scheme='CTCS')
    return p_LW

if __name__=="__main__":
    main()
    
    
