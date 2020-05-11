import qmcpy
discrete_distrib = qmcpy.Lattice(dimension=2)
true_measure = qmcpy.Gaussian(discrete_distrib, mean=0, covariance=1/2)
integrand = qmcpy.QuickConstruct(true_measure, custom_fun=keister)
stopping_criterion = qmcpy.CubLattice_g(integrand, abs_tol=1e-4)
solution,data = stopping_criterion.integrate()