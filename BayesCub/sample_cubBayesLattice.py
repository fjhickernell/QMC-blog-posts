'''
    Example: Integrating Keister integrand using Lattice-Bayesian Cubature.
'''
from qmcpy import *
from numpy import *

tol = .005

integrand = Keister(Lattice(dimension=2, order='linear'))
keister_2d_exact = integrand.exact_integ()
solution, data = CubBayesLatticeG(integrand, abs_tol=tol, n_init=2 ** 5).integrate()
print('Integration error: ', abs(solution - keister_2d_exact) < tol)