import qmcpy
discrete_distrib = qmcpy.Lattice(
    dimension = 2)
true_measure = qmcpy.Gaussian(
    distribution = discrete_distrib,
    mean = 0,
    covariance = 1/2)
integrand = qmcpy.CustomFun(
    measure = true_measure,
    custom_fun = keister)
stopping_criterion = qmcpy.CubQMCLatticeG(
    integrand = integrand,
    abs_tol = 1e-4)