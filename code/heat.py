import numpy as np

nx = 40.	   # Number of points in space
x = np.linspace(0, 1, nx+1)	# spatial variable, with 41 points
dx = 1. / nx
nt = 40. 	   # Number of timesteps
t = 10.
dt = t / nt


