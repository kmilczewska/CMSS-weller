import numpy as np

def initial_bell(x):
    return np.where(x%1. <0.5, np.power(np.sin(2*x*pi),2), 0)

def FTCS(x):
    for n in xrange(nt):
